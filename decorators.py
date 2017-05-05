#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This is a basic example about how to implement a decorator function 
    that replace de decorated function with the inner function."""

def score_original(func):
    def inner(s1,s2):
        lengmax = max(s1.__len__(),s2.__len__())
        result = func(s1,s2)/lengmax
        return result
    return inner
