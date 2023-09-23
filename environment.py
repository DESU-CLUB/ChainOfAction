import openai
import os
import subprocess
import ast

#This is just some sample code to brainstorm for the environment

def create_response():
    ##Creates the API call to ChatGPT
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [{'role': 'system', 'content': 'You are CodeGPT, a helpful code assistant that can solve issues in Python. You will only return the code. DO not attempt to explain it or add additional information'},
        {'role': 'user', 'content': 'I am trying to create a list of numbers from 1 to 10.And then I want to print the list.Do not add any explanation'}
        ]
    )

    ##This is the code that is returned from the API call
    code =response.choices[0]["message"]["content"]
    ##Written into a file
    with open('response.py', 'w') as f:
        f.write(code)

#This runs a python script and returns the output
def run_script(file_path, input_data = None):
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

#This is the main function
#What I plan to do is:
#1. Retrieve a sample from the dataset
#2. Check if sample qn requires input
#3. How do I check for this (('m'))
#4. If needs, will loop through all the test cases

def main():
    #grab dataset qn
    #This is a placeholder, once dataset is settled will concrete this
    create_response() #Will accept a qn statement
    #Actual version will be a for loop that runs the script on all the test cases
    #Outputs will be stored in a
    #list and checked with actual ground truth
    #Sent to evaluation function
    result = run_script('response.py')
    if result.returncode == 0:
        return evaluate(ast.literal_eval(result.stdout), [1,2,3,4,5,6,7,8,9,10])
    #Bad programming practice, but ast eval will only evaluate literals
    #This is as sometimes whitespace may be negligible but messes up the comparison function as it is taking
    #strict string equality -> So instead I will compare literals by eval(literal)
        
    else:
        return 0

def evaluate(pred, y):
    return int(pred == y) #1 if correct, 0 if not


print(main())