""" import os
import ast
from typing import Optional, List, Tuple
from math import inf
import collections
from collections import Counter
from bisect import bisect_left
import re
import json
optionalAPI = '''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
'''
def extract_clean_test_cases_with_values(content):
    # This pattern captures sequences within brackets (assumed to be arrays) and standalone numbers
    # It specifically looks for patterns like "k = <number>" and captures just the number
    pattern = r'\b\w+\s*=\s*'
    cleaned_string = re.sub(pattern, '', content)
    return cleaned_string

def extract_function_signature(code, function_name):
    pattern = rf'def\s+{re.escape(function_name)}\s*\((.*?)\)(\s*->\s*[^\s:]+)?\s*:'
    matches = re.findall(pattern, code)
    if matches:
        params, return_type = matches[0]
        return f"def {function_name}({params}){return_type}:"
    return None

def  get_function_parameters(code, function_name):
    tree = ast.parse(code)
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == function_name:
            # Found the function, now get its arguments
            args = node.args
            # Count the number of positional arguments
            num_args = len(args.args)
            # Check for *args
            vararg = 1 if args.vararg else 0
            # Check for **kwargs
            kwarg = 1 if args.kwarg else 0
            # Return the total number of arguments
            print("Breakdown:",num_args,vararg,kwarg)
            return num_args + vararg + kwarg -1
    

def format_test_case_for_eval(input_str):
    # Helper function to add escaped quotes around strings if they are not numeric or list representations
    pattern = r'(?<!["\'])\b[A-Za-z]+\b(?![\'"])'
    # Strings to test

    # Using re.sub to add quotes around any alphabetical value
    quoted_strings = re.sub(pattern, r"'\g<0>'", input_str)
    return quoted_strings


def is_return_type_str(method_signature: str) -> bool:
    # Regular expression to match return type annotation
    pattern = r'->\s*([^\s:]+)'

    # Find the return type in the method signature
    match = re.search(pattern, method_signature)

    # Check if the return type is 'str'
    return match is None or match.group(1) == 'str'


def func_head(code):
    tree = ast.parse(code)
    fnames = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            fnames.append(node.name)
    return fnames

for file in os.listdir("chainofaction/data/code"):
    with open("chainofaction/data/code/"+file) as f:
        a = f.read()
        if "ListNode" in a or "TreeNode" in a:
            print(file)
            continue
    if file.endswith(".py"):
        if not os.path.exists("chainofaction/data/cases/"+file[:-3]+".txt"):
            print(file)
            continue
        with open("chainofaction/data/cases/"+file[:-3]+".txt") as f:
            cases = f.readlines()
            cfm = []
            print(f)
            for line in cases:
                cur = line.strip()
                if cur.startswith("("):
                    continue
                else:
                    with open("chainofaction/data/code/"+file) as f:
                        code = f.read()
                        exec(optionalAPI)
                        try:
                            exec(code)
                        except:
                            continue
                        funcs = func_head(code)
                        func_map = {}
                        for func in funcs:
                            func_map[func] = extract_function_signature(code, func)
                        listTree = False

                        print(func_map)
                        print("Running",file)
                        cur = cur.replace("Input: ","")
                        for a in funcs:
                            try:
                                if cur == "":
                                    continue
                                if isinstance(eval(cur),list) or isinstance(eval(cur),tuple):
                                    for i in eval(str(cur)):

                                        if str(cur).startswith("("):
                                            output = eval("Solution()."+a+"(*"+str(cur)+")")
                                        else:
                                            output = eval("Solution()."+a+"("+str(cur)+")")
                                        cased = (cur,output)
                                else:
                                    output = eval("Solution()."+a+"("+str(cur)+")")
                                    cased = (format_test_case_for_eval(cur),output)
                                
                                print(cased[0], type(cased[0]))
                                print(cased[1], type(cased[1]))
                                print(is_return_type_str(func_map[a][1]))
                                print(func_map[a])
                                cfm.append({"input": [eval(cased[0])] if type(eval(cased[0])) != tuple else [val for val in eval(cased[0])], "output": cased[1] if  (is_return_type_str(func_map[a]))  else eval(cased[1]) if type(cased[1]) == str else cased[1]})

                            except Exception as e:
                                print(e)


    if cfm != []:
        with open("chainofaction/data/fullcases/"+file[:-3]+".json","w") as f:
                json.dump(cfm,f)
 """


import os
import pandas as pd
import vector_database.vector_database as skills
def load_init_skills(path):
    passages = pd.read_csv(os.path.join(path, "leetcode.tsv"), sep='\t', header=0)
    return passages.head(int(len(passages)*5/100))


docs=  load_init_skills("chainofaction/data")
dataset = "leetcode"
emb_func = skills.MiniLML6V2EmbeddingFunction()
data_dir = "chainofaction/data"
db = skills.ChromaWithUpsert(
        name=f"{dataset}_minilm6v2",
        embedding_function=emb_func,  # you can have something here using /embed endpoint
        persist_directory= "chainofaction/data/"
        )
if db.is_empty():
    db.upsert_texts(
        texts=docs.indextext.tolist(),
        # we handle tokenization, embedding, and indexing automatically. You can skip that and add your own embeddings as well
        metadata=[{'id': id, 'title': title, 'problem_text': problem_text, 'skill_description': skill_description}
                for (id, title, problem_text, skill_description) in
                zip(docs.id, docs.title, docs.problem_text, docs.skill_description)],  # filter on these!
        ids=[str(i) for i in docs.id],  # unique for each doc
    )

print(db.query('''
Problem Link: https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order 
and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.'''))
