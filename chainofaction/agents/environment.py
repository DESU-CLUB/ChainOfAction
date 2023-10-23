import openai
import os
import subprocess
import ast
from chainofaction.skill import skill_library
from chainofaction.agents import skillcreator
#This is just some sample code to brainstorm for the environment

class Environment:
    def __init__(self):
        self.db = ChromaWithUpsert()
        self.init_db()
        self.agent = Agent(self.db)


    def reset(self):
        self.db = ChromawithUpsert()
        self.Agent = Agent(self.db)

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

    def step(problem):
        soln = self.agent.get_response(problem,cases)
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

    def reset:

#def sample_from_dataset():



print(main())