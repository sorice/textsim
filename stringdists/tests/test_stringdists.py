#!/usr/bin/env python

__author__ = 'Abel Meneses-Abad, Pablo Ulacia'

import unittest
import sys
import os
import pytest
import platform
import csv

open_kwargs = {'encoding': 'utf8'}

if platform.python_implementation() == 'CPython':
    implementations = ['python', 'c']
else:
    implementations = ['python']

sys.path.append(os.path.abspath(os.getcwd()))
sys.path.append(os.path.abspath(os.path.join(os.getcwd(),'../../..')))
#     try:
#         from textsim.stringdists import (lcs, lcs_similarity,
#                                         damerau_levenshtein_similarity_textsim)
#     except ImportError:
#         print('ImportError')

# sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(),'..')))
# from ..stringdists import lcs

p = os.path.abspath(os.path.join(os.getcwd(),'data'))
q = os.path.abspath(os.path.join(os.getcwd(),'../../..'))

if os.path.exists(p):
    p = p
else:
    if os.path.exists(q):
        p=q

def _load_data(name):
    with open(p+'data/{}.csv'.format(name), **open_kwargs) as f:
        for data in csv.reader(f):
            yield data

@pytest.fixture(params=implementations)
def ds(request):
    if request.param == 'python':
        from textsim.stringdists import distances as ds
    else:
        from textsim.stringdists import distances as ds
    return ds

@pytest.mark.parametrize('s1, s2,value', _load_data('damerau_levenshtein'), ids=str)
def test_damerau_levenshtein(ds, s1, s2, value):
    value = int(value)
    print('ds',ds)
    assert ds.damerau_levenshtein_distance_jellyfish(s1, s2) == value

# class Testchardists(unittest.TestCase):
#     def test_lcs(self):
#         self.failUnlessEqual(ds.lcs("thisisatest","testing123testing"),"tsitest")
#     def test_lcs_similarity(self):
#         self.failUnlessEqual(lcs_similarity("thisisatest","testing123testing"),0.6363636363636364)
#     def test_damerau_levenshtein(self):
#         self.failUnlessEqual(damerau_levenshtein_similarity_textsim("jellyfish","smellyfishs"),0.7272727272727273)

# if __name__ == '__main__':
#     unittest.main()
