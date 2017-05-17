#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This is a basic example about how to implement a decorator function
    that replace de decorated function with the inner function."""

from .utils import string2vector

def score_original(func):
    def inner(s1,s2):
        maxlen = max(s1.__len__(),s2.__len__())
        result = func(s1,s2)/maxlen
        return result
    return inner

def string2tokenset(func):
    def inner(s1,s2):
        s1 = set([word for word in s1.split()])
        s2 = set([word for word in s2.split()])
        result = func(s1,s2)
        return result
    return inner

def string2vec(func):
    def inner(s1,s2):
        if isinstance(s1,str) and isinstance(s2,str):
            s1,s2 = string2vector(s1,s2)
        else:
            print('Both values need to be string objects')
        result = func(s1,s2)
        return float(result)
    return inner
