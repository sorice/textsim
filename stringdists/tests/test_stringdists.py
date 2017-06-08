#!/usr/bin/env python

"""
String Similarity Distances Tests
==================================

Based on jellyfish source code.

"""

__author__ = 'Abel Meneses-Abad'

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

#Allows to execute pytest from /textsim or /textsim/stringdists/tests/
p = os.path.abspath(os.path.join(os.getcwd(),'data'))
q = os.path.abspath(os.getcwd()+'/textsim/stringdists/tests/data')
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

def assertAlmostEqual(a, b, places=3):
    assert abs(a - b) < (0.1**places)

@pytest.fixture(params=implementations)
def ds(request):
    if request.param == 'python':
        from textsim.stringdists import distances as ds
    else:
        from textsim.stringdists import distances as ds
    return ds


# Tests for NLTK package imported distances
@pytest.mark.parametrize("s1,s2,value", _load_data('binary'), ids=str)
def test_binary_distance_nltk(ds, s1, s2, value):
    value = float(value)
    assert ds.binary_distance(s1, s2) == value

@pytest.mark.parametrize("s1,s2,value", _load_data('levenshtein'), ids=str)
def test_edit_distance_nltk(ds, s1, s2, value):
    value = int(value)
    assert ds.edit_distance_nltk(s1, s2) == value

@pytest.mark.parametrize("s1,s2,value", _load_data('levenshtein'), ids=str)
def test_edit_similarity_nltk(ds, s1, s2, value):
    value = 1 - float(value)/float(max(len(s1),len(s2),1.0))
    assert ds.edit_similarity_nltk(s1, s2) == value

# Tests for Jellyfish package imported distances

@pytest.mark.parametrize("s1,s2,value", _load_data('levenshtein'), ids=str)
def test_levenshtein_distance_jellyfish(ds, s1, s2, value):
    value = int(value)
    assert ds.levenshtein_distance_jellyfish(s1, s2) == value

@pytest.mark.parametrize("s1,s2,value", _load_data('levenshtein'), ids=str)
def test_levenshtein_similarity_jellyfish(ds, s1, s2, value):
    value = 1 - float(value)/float(max(len(s1),len(s2),1.0))
    assert ds.levenshtein_similarity_jellyfish(s1, s2) >= value

@pytest.mark.parametrize("s1,s2,value", _load_data('jaro_distance'), ids=str)
def test_jaro_distance(ds, s1, s2, value):
    value = float(value)
    assertAlmostEqual(ds.jaro_distance(s1, s2), value, places=3)

@pytest.mark.parametrize("s1,s2,value", _load_data('jaro_winkler'), ids=str)
def test_jaro_winkler(ds, s1, s2, value):
    value = float(value)
    assertAlmostEqual(ds.jaro_winkler_distance(s1, s2), value, places=3)

@pytest.mark.parametrize("s1,s2,value", _load_data('hamming'), ids=str)
def test_hamming_distance(ds, s1, s2, value):
    value = int(value)
    assert ds.hamming_distance_jellyfish(s1, s2) == value

@pytest.mark.parametrize('s1, s2,value', _load_data('damerau_levenshtein'), ids=str)
def test_damerau_levenshtein(ds, s1, s2, value):
    value = int(value)
    print('ds',ds)
    assert ds.damerau_levenshtein_distance_jellyfish(s1, s2) == value

@pytest.mark.parametrize("s1,s2,value", _load_data('match_rating_comparison'), ids=str)
def test_match_rating_comparison(ds, s1, s2, value):
    value = {'True': True, 'False': False, 'None': None}[value]
    assert ds.match_rating_comparison(s1, s2) is value

#Test for Pattern package imported distances

@pytest.mark.parametrize('s1, s2,value', _load_data('levenshtein'), ids=str)
def test_levenshtein_distance_pattern(ds, s1, s2, value):
    value = int(value)
    print('ds',ds)
    assert ds.levenshtein_distance_pattern(s1, s2) == value

@pytest.mark.parametrize("s1,s2,value", _load_data('levenshtein'), ids=str)
def test_levenshtein_similarity_pattern(ds, s1, s2, value):
    value = 1 - float(value)/float(max(len(s1),len(s2),1.0))
    assert ds.levenshtein_similarity_pattern(s1, s2) >= value

@pytest.mark.parametrize("s1,s2,value", _load_data('dice'), ids=str)
def test_dice_coefficient_pattern(ds, s1, s2, value):
    value = float(value)
    assertAlmostEqual(ds.dice_coefficient_pattern(s1, s2), value, places=3)

#Tests for smith_waterman_distance

@pytest.mark.parametrize('s1, s2,value', _load_data('smith_waterman'), ids=str)
def test_smith_waterman_distance(ds, s1, s2, value):
    value = float(value)
    assert ds.smith_waterman_distance(s1, s2, 2, -1, 1) == value

#Tests for self Textsim distances

#lcs

#lcs_distance

#lcs_similarity

@pytest.mark.parametrize('s1, s2,value', _load_data('damerau_levenshtein'), ids=str)
def test_damerau_levenshtein_textsim(ds, s1, s2, value):
    value = int(value)
    assert ds.damerau_levenshtein_distance_textsim(s1, s2) == value

@pytest.mark.parametrize("s1,s2,value", _load_data('dice'), ids=str)
def test_sorensen_distance_textsim(ds, s1, s2, value):
    value = float(value)
    assertAlmostEqual(ds.sorensen_distance_textsim(s1, s2), value, places=3)

# needleman_wunch_distance

# needleman_wunch_similarity
