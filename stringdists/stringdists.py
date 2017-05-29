#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
String Similarity Distances
==================================

Based on character similarity calculations.

"""

__author__ = 'Abel Meneses-Abad, Pablo Ulacia'

try:
    from nltk.metrics import edit_distance as edit_distance_nltk2
    from nltk.metrics import binary_distance as binary_distance_nltk
except:
    pass

try:
    from .jellyfish import levenshtein_distance as levenshtein_distance_jellyfish2
    from .jellyfish import jaro_distance as jaro_distance_jellyfish
    from .jellyfish import jaro_winkler as jaro_winkler_distance_jellyfish
    from .jellyfish import hamming_distance as hamming_distance_jellyfish
    from .jellyfish import damerau_levenshtein_distance as damerau_levenshtein_distance_jellyfish2
    from .jellyfish import match_rating_comparison as match_rating_comparison2
except:
    pass

from .pattern import levenshtein as levenshtein_distance_pattern2
from .pattern import levenshtein_similarity as levenshtein_similarity_pattern2

from ..decorators import score_original, Appender
from .distances_doc import *

from .swalign import NucleotideScoringMatrix, LocalAlignment

def lcs(s1, s2):
    """
    :title: Longest Common Sequence

    Devuelve la subsecuencia mas larga [barron-cedeno2013]_

    :math: max(s1 \in s2)

    :brief formula explanation:

    .. topic:: References

    .. [barron-cedeno2013] Barrón-Cedeño Alberto, Vila Marta, Martí M. Antonia,
        Rosso Paolo. 2013.
        Title *"`Plagiarism meets Paraphrasing: Insights for the Next
        Generation in Automatic Plagiarism Detection
        <http://www.mitpressjournals.org/doi/pdf/10.1162/COLI_a_00153>`_"*.
        In *Computational Linguistics*.

    :doctest:

    @param s1, s2: Cadenas a analizar
    @param doc1,doc2: Camino del documento a analizar
    @type s1: str
    @type s2: str
    @rtype str

    >>> s1 = 'thisisatest'
    >>> s2 = 'testing123testing'
    >>> lcs(s1, s2) == 'tsitest'
    True

    """

    lengths = [[0 for j in range(len(s2)+1)] for i in range(len(s1)+1)]
    # row 0 and column 0 are initialized to 0 already
    for i, x in enumerate(s1):
        for j, y in enumerate(s2):
            if x == y:
                lengths[i+1][j+1] = lengths[i][j] + 1
            else:
                lengths[i+1][j+1] = max(lengths[i+1][j], lengths[i][j+1])
    # read the substring out from the matrix
    result = ""
    x, y = len(s1), len(s2)
    while x != 0 and y != 0:
        if lengths[x][y] == lengths[x-1][y]:
            x -= 1
        elif lengths[x][y] == lengths[x][y-1]:
            y -= 1
        else:
            assert s1[x-1] == s2[y-1]
            result = s1[x-1] + result
            x -= 1
            y -= 1
    return result

@Appender(lcs.__doc__)
def lcs_distance(s1,s2):
    """Lenght of LCS.
    """
    return len(lcs(s1,s2))

def lcs_similarity(s1,s2):
    """
    La distancia de longlcs es una medida de comparacion entre dos cadenas la
    cual va a retornar un valor int, tendiendo a n mientras mayor sea la
    semejanza es una modificacion de longlcs, donde n es la longitud de s1.
    En esta implementacion se realizo una modificacion para obtener un valor entre [0-1]
    dividiendo entre la longitud de la cadena mas larga
    @param s1, s2: Cadenas a analizar
    @param doc1,doc2: Camino del documento a analizar
    @type s1: str
    @type s2: str
    @rtype int

    >>> s1 = "jellyfish"
    >>> s2 = "smellyfishs"
    >>>lcs_similarity(s1,s2) == 0.7272727272727273
    True
    """

    arr=lcs(s1, s2)

    if s1<s2:
        tmp=len(s2)
    else:
        tmp=len(s1)
    return float(len(arr))/tmp

def damerau_levenshtein_similarity_textsim(s1, s2):
    """Damerau variation of Levenshtein distance.
    """

    d = {}
    lenstr1 = len(s1)
    lenstr2 = len(s2)
    for i in range(-1,lenstr1+1):
        d[(i,-1)] = i+1
    for j in range(-1,lenstr2+1):
        d[(-1,j)] = j+1

    for i in range(lenstr1):
        for j in range(lenstr2):
            if s1[i] == s2[j]:
                cost = 0
            else:
                cost = 1
            d[(i,j)] = min(
                            d[(i-1,j)] + 1, # deletion
                            d[(i,j-1)] + 1, # insertion
                            d[(i-1,j-1)] + cost, # substitution
                            )
            if i and j and s1[i]==s2[j-1] and s1[i-1] == s2[j]:
                d[(i,j)] = min (d[(i,j)], d[i-2,j-2] + cost) # transposition

    lengthmax = max(s1.__len__(), s2.__len__())

    return 1-float(d[lenstr1-1,lenstr2-1])/lengthmax

# if not NLTKImportError:
@Appender(binary_distance_nltk.__doc__)
def binary_distance(s1,s2):
    if binary_distance_nltk(s1,s2):
        return 0.0
    else:
        return 1.0

@Appender(edit_distance_doc)
def edit_distance_nltk(s1,s2):
    """NLTK implementation of Levenshtein distance, also known as Edit distance.
    """
    return edit_distance_nltk2(s1,s2)

@score_original
@Appender(edit_similarity_doc)
def edit_similarity_nltk(s1,s2):
    """NLTK implementation of Levenshtein similarity.
    """
    return edit_distance_nltk2(s1,s2)

#from Jellyfish package
@Appender(edit_distance_doc)
def levenshtein_distance_jellyfish(s1,s2):
    """Jellyfish implementation of Levenshtein distance, also known as Edit distance.
    """
    return levenshtein_distance_jellyfish2(s1,s2)

@score_original
@Appender(edit_similarity_doc)
def levenshtein_similarity_jellyfish(s1,s2):
    """Levenshtein similarity based on Jellyfish Levenshtein distance.
    """
    return levenshtein_distance_jellyfish2(s1,s2)

@Appender(jaro_dist_doc)
def jaro_distance(s1,s2):
    """Jaro distance based on Jellyfish Jaro distance implementation.
    """
    return jaro_distance_jellyfish(s1,s2)

@Appender(jaro_winkler_dist_doc)
def jaro_winkler_distance(s1,s2):
    """Jaro Winkler distance based on Jellyfish Jaro-Winkler distance implementation.
    """
    return jaro_winkler_distance_jellyfish(s1,s2)

@Appender(hamming_dist_doc)
def hamming_distance(s1,s2):
    """Jaro distance based on Jellyfish Jaro distance implementation.
    """
    return hamming_distance_jellyfish(s1,s2)

@Appender(damerau_levenshtein_dist_doc)
def damerau_levenshtein_distance_jellyfish(s1,s2):
    """Jaro distance based on Jellyfish Jaro distance implementation.
    """
    return damerau_levenshtein_distance_jellyfish2(s1,s2)

@Appender(match_rating_comparison_doc)
def match_rating_comparison(s1,s2):
    """Matching rating comparison.
    """
    return match_rating_comparison2(s1,s2)

#from Pattern package
@Appender(edit_distance_doc)
def levenshtein_distance_pattern(s1,s2):
    """Pattern implementation of Levenshtein distance, also known as Edit distance.
    """
    return levenshtein_distance_pattern2(s1,s2)

@Appender(edit_similarity_doc)
def levenshtein_similarity_pattern(s1,s2):
    """Pattern package implementation of Levenshtein similarity.
    """
    return levenshtein_similarity_pattern2(s1,s2)

#From swalign package
def smith_waterman_distance(s1,s2):
    match = 2
    mismatch = -1
    scoring = NucleotideScoringMatrix(match, mismatch)
    sw = LocalAlignment(scoring)
    tmp=sw.align(s1,s2).matches+sw.align(s1,s2).mismatches
    return float(sw.align(s1,s2).matches)/tmp

@Appender(needleman_wunch_dist_doc)
def needleman_wunch_distance(s1, s2, gap_cost=2):
    """Needleman Wunch distance.
    """

    if isinstance(s1, bytes) or isinstance(s2, bytes):
        raise TypeError(_no_bytes_err)

    if s1 == s2:
        return 0
    rows = len(s1)+1
    cols = len(s2)+1

    if not s1:
        return cols-1
    if not s2:
        return rows-1

    prev = None
    cur = range(cols)
    for r in range(1, rows):
        prev, cur = cur, [r] + [0]*(cols-1)
        for c in range(1, cols):
            deletion = prev[c] + gap_cost
            insertion = cur[c-1] + gap_cost
            edit = prev[c-1] + (0 if s1[r-1] == s2[c-1] else gap_cost)
            cur[c] = min(edit, deletion, insertion)

    return cur[-1]


@score_original
@Appender(needleman_wunch_dist_doc)
def needleman_wunch_similarity(s1,s2):
    """Needleman Wunch distance divided by the maximal length of both strings.
    """
    return needleman_wunch_distance(s1,s2)

if __name__ == '__main__':
    s1=input("Input text A:")
    s2=input("Input text B:")
    print("La subsecuencia mas larga con el metodo LCS es '%s'" % lcs(s1,s2))
    print("LCS distance:",longlcs(s1,s2))
    print("Damerau levenshtein distance:",damerau_levenshtein_similarity_textsim(s1,s2))
