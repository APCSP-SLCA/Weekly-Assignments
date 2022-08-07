import ast, os
import inspect
from typing import NamedTuple

class Violation(NamedTuple):
    """
    Every rule violation contains a node that breaks the rule,
    and a message that will be shown to the user.
    """

    node: ast.AST
    message: str


class Checker(ast.NodeVisitor):
    """
    A Checker is a Visitor that defines a lint rule, and stores all the
    nodes that violate that lint rule.
    """

    def __init__(self, issue_code):
        self.issue_code = issue_code
        self.violations = set()
        return
    
class BannedTokChecker(Checker):
    
    banned_toks = (
        'as,break,class,continue,del,for,' +
        'global,in,lambda,nonlocal,raise,repr,' +
        'while,with,yield,' +
        '__import__,ascii,bin,bytearray,bytes,callable,' +
        'classmethod,compile,delattr,dict,dir,enumerate,' +
        'eval,literal_eval,exec,filter,format,frozenset,getattr,globals,' +
        'hasattr,hash,help,hex,id,issubclass,iter,' +
        'list,locals,map,memoryview,next,object,oct,' +
        'open,ord,property,range,reversed,set,' +
        'setattr,slice,sorted,staticmethod,super,tuple,' +
        'vars,zip,importlib,imp,string,[,],{,}')
    
    def generic_visit(self, node):
#         print(ast.dump(node, indent=4))
        
        if isinstance(node, ast.Name) and node.id == "round":            
            violation = Violation(
                node=node,
                message=f"Do not use builtin \"round\" in Python 3",
            )
            self.violations.add(violation)
        
#         if isinstance(node, ast.Try):
# 
#             violation = Violation(
#                 node=node,
#                 message=f"Disallowed token(s): try-except-finally",
#             )
#             self.violations.add(violation)
# 
#         elif isinstance(node, ast.Try):
# #             print(ast.dump(node, indent=4))
#             violation = Violation(
#                 node=node,
#                 message=f"Disallowed token(s): try-except-finally",
#             )
#             self.violations.add(violation)
            
        super().generic_visit(node)
            
        return

class LinterError(Exception):
    def __init__(self, errors):
        
        message = ""
        for err in errors:
            message += err
        
        super().__init__(message)

class Linter:
    """Holds all list rules, and runs them against a source file."""

    def __init__(self, file_name=None):
        self.checkers = set()
        self.errors = list()
        self.source_code = None
        self.file_name = file_name
        self.pretty_file_name = os.path.basename(file_name)
        
        with open(self.file_name) as file:
            self.source_code = file.read()
        return
    
    @staticmethod
    def print_violations(checker, file_name):
        for node, message in checker.violations:
            print(
                f"{file_name}:{node.lineno}:{node.col_offset}: "
                f"{checker.issue_code}: {message}"
            )
    
    def addError(self, checker, file_name):
        for node, message in checker.violations:
            location = f"{file_name}:{node.lineno}:{node.col_offset}: "
            msg = f"{checker.issue_code}: {message}\n"
            expl = (f"You are using a feature of Python that is not allowed "
                    f"in this\n\t\t\tassignment. You will need to solve this "
                    f"assignment without using\n\t\t\tthat feature.")
                   
            self.errors.append(location + msg + expl)
        return
    
    def addChecker(self, checker):
        self.checkers.add(checker)

    def run(self):
        """Runs all lints on a source file in current directory."""
        
        tree = ast.parse(self.source_code)
        for checker in self.checkers:
            checker.visit(tree)
            self.print_violations(checker, self.pretty_file_name)
            

def lint(file_name=None):
    
    if not file_name:
        try:
            caller = inspect.stack()[1]
            module = inspect.getmodule(caller[0])
            file_name = module.__file__
        except:
            print("Linter cannot find your file!")
        
    linter = Linter(file_name)
    linter.addChecker(BannedTokChecker("T0"))
    linter.run()
        
    return

if __name__=="__main__":
    print("Unit tests should go here!")
    