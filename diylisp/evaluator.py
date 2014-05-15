# -*- coding: utf-8 -*-


from types import Environment, LispError, Closure
from ast import is_boolean, is_atom, is_symbol, is_list, is_closure, is_integer
from asserts import assert_exp_length, assert_valid_definition, assert_boolean
from parser import parse


"""
This is the Evaluator module. The `evaluate` function below is the heart
of your language, and the focus for most of parts 2 through 6.

A score of useful functions is provided for you, as per the above imports,
making your work a bit easier. (We're supposed to get through this thing
in a day, after all.)
"""

# define operators
math_operators = ["+", "-", "/", ">", "<", "mod", "*"]

def evaluate(ast, env):
    """Evaluate an Abstract Syntax Tree in the specified environment."""

    if is_boolean(ast): # imported from ast
      return ast

    if is_integer(ast):
        return ast

    if ast[0]=="quote":
        return ast[1]

    if ast[0]=="atom":
        return is_atom(evaluate(ast[1], env))



    if ast[0]=="eq":
        if is_atom(evaluate(ast[1], env))==False:
            return False

        a = ast[1]
        b = ast[2]
        return a == b

    a = ast[1]
    b = ast[2]

    if is_integer(a) and is_integer(b) and ast[0] in math_operators:
        parsed = parse(ast[0])
        print parsed
        result = a parsed b
        return result





    raise NotImplementedError("DIY")
