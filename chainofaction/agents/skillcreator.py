import os
import json
import glob
import re
from multiprocessing import Pool
from tqdm import tqdm
import torch
import openai
import itertools
import random
import environment
import tiktoken

class NoCasesException(Exception):
    pass

class SolutionNotFoundException(Exception):
    pass

class MemoryList(list): #Sliding window implementation for now
    def __init__(self, *args, max_tokens = 3500):
        super().__init__(*args)
        self.max_tokens = max_tokens
        self.tokenizer = tiktoken.encoding_for_model("gpt-4")
        
    def append(self, item):
        total_tokens = self.check_tokens()
        while len(self.tokenizer.encode(item)) + total_tokens > self.max_tokens:
            self.handle_overflow()
            total_tokens = self.check_tokens()
        super().append(item)

    def check_tokens(self):
        return sum(len(self.tokenizer.encode(item)) for item in self)
    
    def handle_overflow(self):
        self.pop(0)

def generate(messages, max_tokens = 2048, temperature = 0.0, model = "gpt-4"):
    if  model in ["gpt-3.5-turbo", "gpt-4"]:
        params = {
            "model": model,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "messages": messages
        }
        for retry in range(3):
            try:
                return openai.ChatCompletion.create(**params)["choices"][0]["message"]["content"]
            except:
                pass
        raise Exception("Failed to generate")
    
    # For older models, use the completion API with max_tokens=1024
    params = {
        "model": model,
        "max_tokens": min(max_tokens, 1024),
        "temperature": temperature,
        "prompt": messages[-1]
    }
    for retry in range(3):
        try:
            return openai.Completion.create(**params)["choices"][0]["text"]
        except:
            pass

class Agent:
    def __init__(self,db, model = "gpt-4", max_tokens = 2048, temperature = 0.0, explore_ratio = 0.3, max_count = 0):
        self.model = model
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.message = MemoryList(max_tokens = 3500)
        self.db = db
        self.explore_ratio = explore_ratio 
        self.max_count = max_count       

    def get_prompt(self,task):
        with open(f"../prompts/{task}") as f:
            return f.read().strip()

    def decompose(self,problem):
        decompose = self.get_prompt("decompose.txt")
        decompose += "\n\n" + problem
        self.message.append([{"role": "user", "content": decompose}])

        for retry in range(3):
            try:
                skills = generate(decompose, max_tokens = 2048, temperature = 0.0, model = "gpt-4")
                self.message.append({"role": "assistant", "content": skills})
                return skills
            except Exception as e:
                print("Error: Failed to generate response")
                self.message.append({"role":"user","content": f"Failed to execute solution generation: {type(e)}"})
    
    def write_soln(self, problem, skills, max_radius = 1):
        soln_writer = self.get_prompt("soln_writer.txt") 
        soln_writer += "\n\n" + problem
        pattern = r'^(\d+:.*?)(?=\d+:|$)'
        sentences = re.findall(pattern, skills, re.MULTILINE)
        for retry in range(3):
            try:
                skill_index = 0
                while skill_index < len(sentences):
                  skill = sentences[skill_index]
                  ans = self.db.query(skill)
                  if ans: #and random.rand() > self.explore_ratio:(Will implement next)
                    soln_writer+= "\n\nHere is the skill required: \n" + skill + "\n\n Here is the Python code: \n"+ans
                  else:
                    """   if self.max_count < 3:
                         newAgent = Agent()
                         ans = newAgent.get_response(skill, self.max_count+1)
                         soln_writer+= "\n\nHere is the skill required: \n" + skill + "\n\n Here is the Python code: \n"+ans """
                    
                    for i in range(max_radius):
                        if skill<len(sentences)-i:
                            skill = skill+ skill[skill_index+i] #Merge the steps
                            ans = self.db.query(skill)
                            if ans:
                              break  
                                
                        if ans:
                            soln_writer+= "\n\nHere is the skill required: \n" + skill + "\n\n Here is the Python code: \n"+ans
                        else:
                            soln_writer += "\n\n Here is the skill required: \n" + skill + "\n\n There is no code given for this skill"

                response = generate(soln_writer, max_tokens = 2048, temperature = 0.0, model = "gpt-4")
                soln = "\n\n".join(re.findall(r"```python\n(.*?)```", response,  re.DOTALL))
                return soln
            except Exception as e:
                print("Error: Failed to generate response")
                self.message.append({"role":"user","content": f"Failed to execute solution generation: {type(e)}"})
        

    
    def rewrite_soln(self, problem, steps, output, retry = 0):
        rewrite = self.get_prompt("soln.txt")
        rewrite += problem + "\n\n" + output
        pattern = r'^(\d+:.*?)(?=\d+:|$)'
        skills = re.findall(pattern, steps, re.MULTILINE)

        for retry in range(3):
            try:
                skill_index = 0
                skills_used = []
                skill = skills[skill_index]
                while skill_index < len(skills):
                    relevant_chunks = self.db.query([skill],n_results = 3)
                    skills_accepted = []
                    for i, chunk in enumerate(relevant_chunks['documents'][0]):
                        if relevant_chunks['distances'][0]['i'] > 0.8:
                            skills_accepted.append(chunk)
                            skills_used.append(chunk)
                    if len(skills_accepted) == 0:
                        skill_index +=1
                        skill = skill[skill_index-1] + " " +skill[skill_index]
                    else:
                        skill_index +=1
                        skill = skill[skill_index]

                    self.message.append({"role":"user",})
                    soln = generate(rewrite, max_tokens = 2048, temperature = 0.0, model = "gpt-4")
                    self.message.append({"role": "assistant", "content": soln})
            except Exception as e:
                print("Error: Failed to generate response")
                self.message.append({"role":"user","content": f"Failed to execute solution generation: {type(e)}"})
            return soln
    def zeroshot_soln(self, problem):
        try:
            self.message.append({"role": "user", "content": f"Here is the problem: {problem}\nWrite Python code to solve the problem"})
            soln = generate(self.message)
            self.message({"role":"user","content": f"Here is the solution: {soln}"})
            return soln
        except Exception:
            return None
    
    

    def get_response(self,problem, cases, max_count = 0):
        '''
        problem: description of problem
        '''
        success = True

        steps = self.decompose(problem)

        soln = self.zeroshot_soln(problem, steps)
        
        if not soln:
            return None

        ###Iterative prompting
        for retry in range(10):
            #TODO
            #Check if code can get correct answer for test cases
            #If not, prompt for more code
            try:
                retry = 0
                passed = True #Dummy variables
                output = ''
                output, passed = environment.execute(soln, cases) #Environment implemented in env.py later
                for i in range(10):
                    if passed:
                        break
                    soln = self.rewrite_soln(problem, steps,output,retry = retry)
                    output, passed = environment.execute(soln, cases)
                break

                    
            except Exception as e:
                print("Error: Failed to generate response")
                self.message.append({"role":"user","content": f"Failed to execute iterative prompting: {type(e)}"})

        if not passed:
            success = False

        #save into chroma before return statement
        if success:
            self.message.append({"role": "user", "content": f"Write a description of what this program solves {soln}"})
            desc = generate(self.message)
            self.message.append({"role": "user", "content": f"Here is the description: {desc}"})
            return (soln, desc)
        return None

    def reset(self):
        self.message = MemoryList(max_tokens = 3500)