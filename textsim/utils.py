#!/usr/bin/env python

import textsim
from sklearn.feature_extraction.text import CountVectorizer
from collections import deque

def calc_all(s1,s2):
    """Sort the available distances in textsim lib and calculate them.
    Return a list with all measures."""
    sim_vector = []
    sim_vector.extend([s1,s2])
    #To control the order of features in Machine Learning experiments.
    metrics = sorted(textsim.__all_distances__.keys())
    for metric in metrics:
        value = textsim.__all_distances__[metric](s1, s2)
        #The next flow is to facilitate sklearn-cvs and weka-arff further
        #generation on big text data collections.
        if str(value) == 'True':
            sim_vector.append(1.0)
        elif str(value) == 'False':
            sim_vector.append(0.0)
        else:
            sim_vector.append(value)
    return sim_vector

def string2vector(s1,s2):
    """Return both strings into its correspondent vector inside the 
    matrix of token counts.

    :Example:

    >>>from textsim.utils import string2vector
    >>>s1 = "John Smith eat a fish"
    >>>s2 = "John eat one fish"
    >>>string2vector(s1,s2)
    (array([[1, 1, 1, 0, 1]]), array([[1, 1, 1, 1, 0]]))

    A human readable version of this result could be:

    |      | eat  | fish | john | smith | one  |
    | ---- | ---- | ---- | ---- | ----- | ---- |
    | s1   | 1    | 1    | 1    | 0     | 1    |
    | s2   | 1    | 1    | 1    | 1     | 0    |

    :Note: Notice that CountVectorizer imported from sklearn deletes the
    token 'a' in the first sentence, even with stop_words parameter = None.
    The reason for that is the parameter token_pattern that select by default
    all tokens of 2 or more characters.
    """
    count_v = CountVectorizer()
    tdm = count_v.fit_transform([s1, s2])
    s1 = tdm[0].toarray()
    s2 = tdm[1].toarray()
    return s1,s2

def bigrams(s):
    """Generate char bigrams."""
    return set(s[i:i+2] for i in range(len(s)-1))

def _make_ngrams(l, n):
    """Ngrams generation func.

    :Note: This implementation comes from Takelab system.
    """
    rez = [l[i:(-n + i + 1)] for i in range(n - 1)]
    rez.append(l[n - 1:])
    return zip(*rez)

def string2ngrams(s1,s2,n):
    """Return both strings converted in n-consecutive grams.
    :rtype: deque collection"""
    if isinstance(s1, str) and isinstance(s2,str):
        A = _make_ngrams(s1.split(),n)
        B = _make_ngrams(s2.split(),n)
    else:
        A = _make_ngrams(s1,n)
        B = _make_ngrams(s2,n)
    return deque(A), deque(B)

if __name__ == '__main__':
    print ()
