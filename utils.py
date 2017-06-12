#!/usr/bin/env python

import textsim
from sklearn.feature_extraction.text import CountVectorizer

def calc_all(s1,s2):
    sim_vector = []
    sim_vector.extend([s1,s2])
    metrics = textsim.__all_distances__
    for metric in metrics.values():
        sim_vector.append(metric(s1, s2))
    return sim_vector

def string2vector(s1,s2):
    count_v = CountVectorizer()
    tdm = count_v.fit_transform([s1, s2])
    s1 = tdm[0].toarray()
    s2 = tdm[1].toarray()
    return s1,s2

def bigrams(s):
    """Generate char bigrams."""
    return set(s[i:i+2] for i in range(len(s)-1))

if __name__ == '__main__':
    print ()
