import openai
import os
import subprocess
import ast
import skillcreator
import skills
#This is just some sample code to brainstorm for the environment

class Environment:
    def __init__(self):
        self.db = skills.ChromaWithUpsert()
        self.init_db()
        self.agent = skillcreator.Agent(self.db)
        self.running_id = 0


    def reset(self):
        self.db = skills.ChromawithUpsert()
        self.Agent = skillcreator.Agent(self.db)

    def init_db(self):
        self.db.init()

    #This runs a python script and returns the output
    def run_script(self, file_path, input_data = None):
        try:
            if input_data is None:
                result = subprocess.run(['python', file_path],
                    text=True,
                    capture_output=True,
                    check=False)
            result = subprocess.run(['python', file_path],
                    input = input_data,
                    text=True,
                    capture_output=True,
                    check=False)
            return result
        except subprocess.CalledProcessError as e:
            return None

    def step(self, problem, cases):
        soln = self.agent.get_response(problem,cases)
        if soln:
            code, desc, title = soln
            texts = "\n".join([str(self.running_id),str(title),(problem),(desc)])
            self.db.upsert_texts(texts, 
                                metadata = [{"id": self.running_id, "title":title,"problem_text":problem,"skill_description":desc}\
                                            for (self.running_id, title, problem, desc) in zip(id, title, problem, desc)
                                            ])
            self.running_id+=1
        return soln

    #This is the main function
    #What I plan to do is:
    #1. Retrieve a sample from the dataset
    #2. Check if sample qn requires input
    #3. How do I check for this (('m'))
    #4. If needs, will loop through all the test cases

    def execute(self, code, cases):
        #placeholder
        pass


    




