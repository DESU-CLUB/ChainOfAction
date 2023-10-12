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

class NoCasesException(Exception):
    pass

class SolutionNotFoundException(Exception):
    pass


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
    def __init__(self, model = "gpt-4", max_tokens = 2048, temperature = 0.0):
        self.model = model
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.message = []
        

    def get_prompt(self,task):
        with open(f"../prompts/{task}") as f:
            return f.read().strip()

    def decompose(self,problem):
        decompose = self.get_prompt("decompose.txt")
        self.message.append([{"role": "user", "content": decompose}])

        for retry in range(3):
            try:
                skills = generate(decompose, max_tokens = 2048, temperature = 0.0, model = "gpt-4")
                self.message.append({"role": "assistant", "content": skills})

            except Exception as e:
                print("Error: Failed to generate response")
                self.message.append({"role":"user","content": f"Failed to execute solution generation: {type(e)}"})
            return skills
    
    def write_soln(self, skills):
        soln_writer = self.get_prompt("soln_writer.txt") 
        for retry in range(3):
            try:
                #Add skill search here to find for relevant skills
                #Below is just some psuedo code

                #fetch = chromadb()
                #skill_list = []
                #some code here to scrape relevant code from the skills
                #for skill in skills:
                #    if fetch.fetch(skill):
                #       skill_list.append(fetch.fetch(skill))
                #    else:
                #        if max_count < 3:
                #           newAgent = Agent()
                #           skill_list.append(newAgent.get_response(skill, cases, max_count+1))
                #        else:
                #           pass

                response = generate(soln_writer, max_tokens = 2048, temperature = 0.0, model = "gpt-4")
                self.message.append({"role": "assistant", "content": skills})
                soln = "\n\n".join(re.findall(r"```python\n(.*?)```", response,  re.DOTALL))
            except Exception as e:
                print("Error: Failed to generate response")
                self.message.append({"role":"user","content": f"Failed to execute solution generation: {type(e)}"})

        return soln if soln else SolutionNotFoundException("Failed to generate solution")



    def get_response(self,problem, cases = None, max_count = 0):
        '''
        problem: description of problem
        '''
        #TODO Add skill library usage


        val = self.decompose(problem)

        soln = self.write_soln()
        
        if isinstance(soln, SolutionNotFoundException):
            raise soln


        if not cases:
            for retry in range(3):
                try:
                    make_test = self.get_prompt("make_test.txt")
                    self.messages.append({"role":"user","content": make_test})
                    cases = generate(self.messages)
                except Exception as e:
                    print(f"Error: Failed to generate response: {type(e)}")
        
        if cases == None:
            raise Exception("Failed to generate test cases")

        ###Iterative prompting
        for retry in range(10):
            #TODO
            #Check if code can get correct answer for test cases
            #If not, prompt for more code
            try:
                passed = True #Dummy variables
                output = ''
                #output, passed = environment.execute(soln, cases) #Environment implemented in env.py later
                prompt = self.get_prompt("iterative_prompt.txt")
                while not passed:
                    prompt += "\n\n" + output
                    self.message.append({"role": "user", "content": prompt})
                    soln = generate(self.message)
                    #output, passed = environment.execute(soln, cases)

                    
            except:
                print("Error: Failed to generate response")
                self.message.append({"role":"user","content": f"Failed to execute iterative prompting: {type(e)}"})


        #save into chroma before return statement
        return soln
