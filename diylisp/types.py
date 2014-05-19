# -*- coding: utf-8 -*-

"""
This module holds some types we'll have use for along the way.

It's your job to implement the Closure and Environment types.
The LispError class you can have for free :)
"""
import re
re_integer = re.compile('[0-9]+')
re_symbol = re.compile('[a-zA-Z*/<>+=-]+')

class LispError(Exception): 
    """General lisp error class."""
    pass

class Closure:
    
    def __init__(self, env, params, body):
        self.env = env
        self.params = params
        self.body = body


    def __str__(self):
        return "<closure/%d>" % len(self.params)

class Environment:

    def __init__(self, variables=None):
        self.variables = variables if variables else {}

    def lookup(self, symbol):
        if symbol in self.variables:
            return self.variables[symbol]
        else: raise LispError(symbol)

    def extend(self, variables):
        new = self.variables.copy()
        new.update(variables)
        return Environment(new)

    def set(self, symbol, value):
        if symbol in self.variables:
            raise LispError("already defined")
        return self.variables.update({symbol: value})

