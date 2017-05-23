#####!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Combined Similarity Distances
==================================

Based on combination of similarity distances based on Token, Corpus, Syntactic
data structures, Corpus and Knowledge distances.

This module contain calls to different self implementations of
combined distances that appear on international papers about
Plagiarism Identification and Text-Reuse Detection.

"""

__author__ = 'Abel Meneses-Abad'

import nltk
from nltk.corpus import wordnet as ws
from ..stringdists import damerau_levenshtein_distance_textsim as damerau_levenshtein_distance
from ..decorators import string2tokenset

@string2tokenset
def jaccard_ulacia_distance(s1,s2):
    """Modificacion de la medida Jaccard utilizando wordnet para expandir la busqueda

    @param s1, s2: Cadenas a analizar
    @type s1: str
    @type s2: str
    @rtype: float

    >>> import nltk
    >>> from nltk.corpus import wordnet as ws
    >>> x = "my house is pretty"
    >>> y = "the house my is pretty"
    >>> jaccard_ulacia(x, y) == 1
    True
    """

    contador=0

    for i in s1:
        for j in s2:
            try:
                tmp1=ws.synsets(i)[0]
                tmp2=ws.synsets(j)[0]
                similitud=tmp1.wup_similarity(tmp2)
                similitud2=tmp1.path_similarity(tmp2)
                if similitud>=similitud2:
                    tmp=similitud
                else:
                    tmp=similitud2
                if tmp>0.75:
                    contador+=1
                    break
            except:
                if len(i)<len(j):
                    tmp=float(damerau_levenshtein_distance(i, j))
                else:
                    tmp=float(damerau_levenshtein_distance(i, j))
                if tmp<0.3:
                    contador+=1
                    break

    if float(len(s1.union(s2))) == 0:
        result = 'inf'
    else:
        result = contador/float(len(s1.union(s2)))
    return result

if __name__ == '__main__':
        v1="PCCW's chief operating officer, Mike Butcher, and Alex Arena, the chief financial officer, will report directly to Mr So."
        v2="Current Chief Operating Officer Mike Butcher and Group Chief Financial Officer Alex Arena will report to So."
        print("jaccard_ulacia distance:",jaccard_ulacia(v1,v2))
