from _ast import AsyncFunctionDef, ClassDef, FunctionDef
import ast
from typing import Any
import astunparse


class FunctionVisitor(ast.NodeVisitor):
    def __init__(self):
        self.functions = []

    def _process(self, node, is_async, class_name = None):
        decorators = [ast.dump(decorator, annotate_fields=False)
                      for decorator in node.decorator_list]
        parameters = [param.arg for param in node.args.args]
        body = astunparse.unparse(node.body)
        function_name = f"{class_name}.{node.name}" if class_name else node.name
        self.functions.append({'decorators': decorators,
                               'name': function_name,
                               'async': is_async,
                               'parameters': parameters,
                               "body": body})
        
        self.generic_visit(node)

    def process_function(self, node, is_async, class_name = None):
        self._process(node, is_async, class_name)

    def process_method(self,node,class_name = None):
        is_async = isinstance(node, ast.AsyncFunctionDef)
        self._process(node, is_async, class_name)

    def visit_FunctionDef(self, node: FunctionDef, class_name = None) -> Any:
        self.process_function(node,is_async= False)

    def visit_AsyncFunctionDef(self, node: AsyncFunctionDef, class_name = None) -> Any:
        self.process_function(node, is_async=  True)

    def visit_ClassDef(self, node: ClassDef) -> Any:
        for item in node.body:
            if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                self.process_method(item, class_name = node.name)
            else:
                self.generic_visit(node)

class Parser:
    def __init__(self):
        self.visitor = FunctionVisitor()

    def analyze_code(self, code):
        tree = ast.parse(code)
        visitor = FunctionVisitor()
        visitor.visit(tree)
        
        for func in visitor.functions:
            print(f"Function decorators: {func['decorators']}")
            print(f"Function name: {func['name']}")
            print(f"Function parameters: {func['parameters']}")
            print(f"Function type: {func['async']}")
            print(f"Function body: {func['body']}")

    def grab_functions(self):
        return self.visitor.functions
    



a = Parser()

a.analyze_code("""
class a:
    async def foo(hi):
        pass

    @hello           
    def bar():
        pass
               
def wew():
    pass

""")
