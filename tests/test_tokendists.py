#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Pablo Ulacia, Abel Meneses-Abad'

import nltk
import math
from nltk.tokenize import word_tokenize
from nltk import *
import unittest
import pytest
import platform, sys, os
import csv

open_kwargs = {'encoding': 'utf8'}

if platform.python_implementation() == 'CPython':
    implementations = ['python', 'c']
else:
    implementations = ['python']

sys.path.append(os.path.abspath(os.getcwd()))

#Allows to execute pytest from /textsim or /textsim/tokendists/tests/
p = os.path.abspath(os.path.join(os.getcwd(),'data'))
q = os.path.abspath(os.getcwd()+'/textsim/tokendists/tests/data')
print(q)

if os.path.exists(p):
    p = p
    print('sí existe')
elif os.path.exists(q):
    p = q
else:
    print('Nither of both directions')

def _load_data(name):
    with open(p+'/{}.csv'.format(name), **open_kwargs) as f:
        for data in csv.reader(f):
            yield data

def assertAlmostEqual(a, b):
    assert abs(a - b) < (0.1**2)

@pytest.fixture(params=implementations)
def ds(request):
    if request.param == 'python':
        from textsim.tokendists import distances as ds
    else:
        from textsim.tokendists import distances as ds
    return ds

def test_vector(ds):
    assertAlmostEqual(ds.euclidean_distance_textsim("0.1 0.2 0.3 0.4","0.1 0.2 0.3 0.5"),1.0)
    assertAlmostEqual(ds.overlap_distance_textsim("0.1 0.2 0.3 0.4","0.1 0.2 0.3 0.5"),0.75)
    assertAlmostEqual(ds.manhattan_distance_sklearn("0.1 0.2 0.3 0.4","0.1 0.2 0.3 0.5"),1.0)
    assertAlmostEqual(ds.matching_coefficient_textsim("0.1 0.2 0.3 0.4","0.1 0.2 0.3 0.5"), 0.75)
    assertAlmostEqual(ds.dice_coefficient_textsim("0.1 0.2 0.3 0.4","0.1 0.2 0.3 0.5"),0.6)
    assertAlmostEqual(ds.cosine_distance_sklearn("0.1 0.2 0.3 0.4","0.1 0.2 0.3 0.5",),0.75)
    assertAlmostEqual(ds.masi_distance("0.1 0.2 0.3 0.4","0.1 0.2 0.3 0.5"),0.802)
    #assertAlmostEqual(ds.jaccard_ulacia("my house is pretty","the house my is pretty"),1.0)

@pytest.mark.parametrize("s1,s2,value", _load_data('jaccard'), ids=str)
def test_jaccard_distance_textsim(ds, s1, s2, value):
    value = float(value)
    assert ds.jaccard_distance_textsim(s1, s2) == value

if __name__ == '__main__':
    unittest.main()
