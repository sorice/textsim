#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This is a basic example about how to implement a decorator function
    that replace de decorated function with the inner function."""

from .utils import string2vector, string2ngrams
from functools import wraps

def score_original(func):
    @wraps(func)
    def inner(s1,s2):
        maxlen = max(s1.__len__(),s2.__len__(),1.0)
        result = func(s1,s2)/maxlen
        return result
    return inner

def string2tokenset(func):
    @wraps(func)
    def inner(s1,s2):
        if isinstance(s1,str) and isinstance(s2,str):
            s1 = set([word for word in s1.split()])
            s2 = set([word for word in s2.split()])
        if isinstance(s1,list) and isinstance(s2,list):
            s1 = set(s1)
            s2 = set(s2)
        result = func(s1,s2)
        return result
    return inner

def string2vec(func):
    @wraps(func)
    def inner(s1,s2):
        if isinstance(s1,str) and isinstance(s2,str):
            s1,s2 = string2vector(s1,s2)
        elif isinstance(s1,list) and isinstance(s2,list):
            s1,s2 = s1,s2
        else:
            print('Both values need to be string objects or numerical vectors!')
        result = func(s1,s2)
        return float(result)
    return inner

def string2qgrams(func):
    @wraps(func)
    def inner(s1,s2,**param):
        if isinstance(s1,str) and isinstance(s2,str):
            if 'n' in param:
                s1,s2 = string2ngrams(s1,s2,param['n'])
            else:
                s1,s2 = string2ngrams(s1,s2,n=1)
        elif not isinstance(s1,str) and not isinstance(s2,str):
            if 'n' in param:
                s1,s2 = string2ngrams(s1,s2,param['n'])
            else:
                s1,s2 = string2ngrams(s1,s2,n=1)
        else:
            print('Both values need to be same type objects')

        result = func(s1,s2,**param)
        return float(result)
    return inner



#This is the original code of Appender class from pandas.utils.decorators
class Appender(object):
    """
    A function decorator that will append an addendum to the docstring
    of the target function.

    This decorator should be robust even if func.__doc__ is None
    (for example, if -OO was passed to the interpreter).

    Usage: construct a docstring.Appender with a string to be joined to
    the original docstring. An optional 'join' parameter may be supplied
    which will be used to join the docstring and addendum. e.g.

    add_copyright = Appender("Copyright (c) 2009", join='\n')

    @add_copyright
    def my_dog(has='fleas'):
        "This docstring will have a copyright below"
        pass
    """
    def __init__(self, addendum, join='', indents=0):
        if indents > 0:
            self.addendum = indent(addendum, indents=indents)
        else:
            self.addendum = addendum
        self.join = join

    def __call__(self, func):
        func.__doc__ = func.__doc__ if func.__doc__ else ''
        self.addendum = self.addendum if self.addendum else ''
        docitems = [func.__doc__, self.addendum]
        func.__doc__ = self.join.join(docitems)
        return func
