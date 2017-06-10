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
    assertAlmostEqual(ds.jaccard_distance("0.1 0.2 0.3 0.4","0.1 0.2 0.3 0.5",None, None,'english'),0.6)
    assertAlmostEqual(ds.euclidean_("0.1 0.2 0.3 0.4","0.1 0.2 0.3 0.5",None, None,'english'),1.0)
    assertAlmostEqual(ds.overlap("0.1 0.2 0.3 0.4","0.1 0.2 0.3 0.5",None, None,'english'),0.75)
    assertAlmostEqual(ds.manhattan("0.1 0.2 0.3 0.4","0.1 0.2 0.3 0.5",None, None,'english'),1.0)
    assertAlmostEqual(ds.matching_coefficient("0.1 0.2 0.3 0.4","0.1 0.2 0.3 0.5",None, None,'english'), 0.75)
    assertAlmostEqual(ds.dice_coefficient("0.1 0.2 0.3 0.4","0.1 0.2 0.3 0.5",None, None,'english'),0.6)
    assertAlmostEqual(ds.cos("0.1 0.2 0.3 0.4","0.1 0.2 0.3 0.5",None, None,'english'),0.75)
    assertAlmostEqual(ds.masi_distance("0.1 0.2 0.3 0.4","0.1 0.2 0.3 0.5",None, None,'english'),0.802)
    assertAlmostEqual(ds.jaccard_ulacia("my house is pretty","the house my is pretty",'english'),1.0)

def test_doc(ds):
    assertAlmostEqual(ds.jaccard(None,None,'c.txt','d.txt','english'),0.6)
    assertAlmostEqual(ds.euclidean(None,None,'c.txt','d.txt','english'),1.0)
    assertAlmostEqual(ds.overlap(None,None,'c.txt','d.txt','english'),0.75)
    assertAlmostEqual(ds.manhattan(None,None,'c.txt','d.txt','english'),1.0)
    assertAlmostEqual(ds.matching_coefficient(None,None,'c.txt','d.txt','english'),0.75)
    assertAlmostEqual(ds.dice_coefficient(None,None,'c.txt','d.txt','english'),0.6)
    assertAlmostEqual(ds.cos(None,None,'c.txt','d.txt','english'),0.75)
    assertAlmostEqual(ds.masi_distance(None,None,'c.txt','d.txt','english'),0.802)
    assertAlmostEqual(ds.jaccard_ulacia(None,None,'jaccard_modificado1.txt','jaccard_modificado2.txt','english'),1.0)

def test_spellcheck_paraprhase(ds):
    """ejemplo de como escribir el paraphrase_example.txt
    el niño come pescado, el muchacho de Maria engullo el peje velozmente,0.09090909090909091
    """
    with open('paraphrase_examples_jaccard.txt') as f:
        for line in f:
            data = line.split(',')
            assertAlmostEqual(ds.jaccard(data[0],data[1],None,None,'spanish'),float(data[2].strip()))
    with open('paraphrase_examples_binary_distance.txt') as f:
        for line in f:
            data = line.split(',')
            assertAlmostEqual(ds.binary_distance(data[0],data[1],None,None,'spanish'),float(data[2].strip()))
    with open('paraphrase_examples_euclidean.txt') as f:
        for line in f:
            data = line.split(',')
            assertAlmostEqual(ds.euclidean(data[0],data[1],None,None,'spanish'),float(data[2].strip()))
    with open('paraphrase_examples_overlap.txt') as f:
        for line in f:
            data = line.split(',')
            assertAlmostEqual(ds.overlap(data[0],data[1],None,None,'spanish'),float(data[2].strip()))
    with open('paraphrase_examples_manhattan.txt') as f:
        for line in f:
            data = line.split(',')
            assertAlmostEqual(ds.manhattan(data[0],data[1],None,None,'spanish'),float(data[2].strip()))
    with open('paraphrase_examples_matching_coefficient.txt') as f:
        for line in f:
            data = line.split(',')
            assertAlmostEqual(ds.matching_coefficient(data[0],data[1],None,None,'spanish'),float(data[2].strip()))
    with open('paraphrase_examples_dice_coefficient.txt') as f:
        for line in f:
            data = line.split(',')
            assertAlmostEqual(ds.dice_coefficient(data[0],data[1],None,None,'spanish'),float(data[2].strip()))
    with open('paraphrase_examples_cos.txt') as f:
        for line in f:
            data = line.split(',')
            assertAlmostEqual(ds.cos(data[0],data[1],None,None,'spanish'),float(data[2].strip()))
    with open('paraphrase_examples_masi_distance.txt') as f:
        for line in f:
            data = line.split(',')
            assertAlmostEqual(ds.masi_distance(data[0],data[1],None,None,'spanish'),float(data[2].strip()))

if __name__ == '__main__':
    unittest.main()
