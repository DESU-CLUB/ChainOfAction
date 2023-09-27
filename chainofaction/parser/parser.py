from _ast import AsyncFunctionDef
import ast
from typing import Any

class FunctionVisitor(ast.NodeVisitor):
    def __init__(self):
        self.functions = []
        self.async_functions = []
        self.decorators_exist = False

    def visit_FunctionDef(self,node):
        self.functions.append(node.name)
        if node.decorator_list :
            self.decorators_exist = True
        self.generic_visit(node)

    def visit_AsyncFunctionDef(self, node: AsyncFunctionDef) -> Any:
        self.async_functions.append(node.name)
        if node.decorator_list:
            self.decorators_exist = True
        self.generic_visit(node)



class Parser:
    def __init__(self,codefile: str):
        self.visitor = FunctionVisitor()
        self.codefile = codefile

    def analyze_file(self):
        with open(self.codefile, 'r') as file:
            tree = ast.parse(file.read(), filename = self.codefile)

        visitor = FunctionVisitor()
        visitor.visit(tree)
        print("Functions in the file", visitor.functions)
        print("Asynchronous functions in the file:", visitor.async_functions)
        print("Decorators exist in the file:", visitor.decorators_exist)


#analyze_file('py')