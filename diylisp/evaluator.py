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


    # ast = boolean
    if is_boolean(ast):
      return ast

    # ast = integer
    if is_integer(ast):
        return ast

    # ast starts with "quote"
    if ast[0]=="quote":
        return ast[1]

    if ast[0]=="atom":
        return is_atom(evaluate(ast[1], env))


    if ast[0]=="eq":
        if is_atom(evaluate(ast[1], env))==False:
            return False

        a = evaluate(ast[1], env)
        b = evaluate(ast[2], env)
        return a == b

    if ast[0] in math_operators:
        a = evaluate(ast[1], env)
        b = evaluate(ast[2], env)
        if is_integer(a) and is_integer(b):

            if ast[0]=="+":
                return a + b
            if ast[0]=="*":
                return a * b
            if ast[0]=="-":
                return a - b
            if ast[0]=="/":
                return a / b
            if ast[0]=="mod":
                return a % b
            if ast[0]==">":
                return a > b
            if ast[0]=="<":
                return a < b

    if ast[0]=="if":
        if evaluate(ast[1], env)==True:
            return evaluate(ast[2], env)
        if evaluate(ast[1], env)==False:
            return evaluate(ast[3], env)

    if is_symbol(ast):
        return env.lookup(ast)

    if ast[0]=="define":
        if not len(ast)==3:
            raise LispError("Wrong number of arguments")
        if not is_symbol(ast[1]):
            raise LispError("non-symbol")
        s = ast[1]
        v  = evaluate(ast[2], env)
        env.set(s, v)
        print s
        return s

    if ast[0]=="lambda":
        print ast[0]
        print ast[0]
        if not len(ast)==3:
            raise LispError("number of arguments")
        if not is_list(ast[1]):
            raise LispError("params not a list")
        return Closure(env, ast[1], ast[2])


    if is_closure(ast[0]):
        closure = ast[0]
        arguments = ast[1:]
        parameters = closure.params
        m = len(parameters)
        n = len(arguments)
        if not n == m:
            raise LispError("wrong number of arguments, expected %d got %d" % ((m), n))
        for i in range(n):
            closure.env.set(parameters[i], evaluate(arguments[i], env))
        return evaluate(closure.body, closure.env)


    if is_symbol(ast[0]):
        clos = env.lookup(ast[0])
        print clos
        arguments = ast[1:]
        parameters = clos.params
        m = len(parameters)
        n = len(arguments)
        if not n == m:
            raise LispError("wrong number of arguments, expected %d got %d" % ((m), n))
        for i in range(n):
            clos.env.set(parameters[i], evaluate(arguments[i], env))
        return evaluate(clos.body, clos.env)

    if is_list(ast[0]):
        clos = evaluate(ast[0], env)
        print clos
        arguments = ast[1:]
        parameters = clos.params
        m = len(parameters)
        n = len(arguments)
        if not n == m:
            raise LispError("wrong number of arguments, expected %d got %d" % ((m), n))

        for i in range(n):
            clos.env.set(parameters[i], evaluate(arguments[i], env))
        return evaluate(clos.body, clos.env)
    else: raise LispError("not a function")


    print ast
    raise LispError("Not able to evaluate")
