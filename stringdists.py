#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
String Similarity Distances
==================================

Based on character similarity calculations.

"""

__author__ = 'Abel Meneses-Abad, Pablo Ulacia'

try:
    from jellyfish import *
except:
    print("'jellyfish package isn't installed.")
    pass

def lcs(s1, s2):
    """
    Devuelve la subsecuencia mas larga
    @param s1, s2: Cadenas a analizar
    @param doc1,doc2: Camino del documento a analizar
    @type s1: str
    @type s2: str
    @rtype str

    >>> s1 = 'thisisatest'
    >>> s2 = 'testing123testing'
    >>> lcs(s1, s2) == 'tsitest'
    True
    Longest common subsequence - Rosetta Code.htm
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
        
def longlcs(s1,s2):
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
    >>>longlcs(s1,s2) == 0.7272727272727273
    True
    """              
    
    arr=lcs(s1, s2)

    if s1<s2:
        tmp=len(s2)
    else:
        tmp=len(s1)
    return float(len(arr))/tmp       

def damerau_levenshtein_distance(s1, s2):
    """
    La distancia de Damerau es una medida de comparacion entre dos cadenas la
    cual va a retornar un valor int, tendiendo a 0 mientras mayor sea la
    semejanza.
    En esta implementacion se realizo una modificacion para obtener un valor entre [0-1]
    donde cuando tiende a 1 es que existe mayor similitud y cuando tiende a 0 tiene menor 
    similitud.
    Esta operacion se realizo dividiendo entre la longitud de la cadena mas larga y restando el resultado 
    con 1 para invertir el orden a que esta tendiendo
    @param s1, s2: Cadenas a analizare
    @type s1: str
    @type s2: str
    @rtype int

    >>> s1 = "jellyfish"
    >>> s2 = "smellyfishs"
    >>>damerau_levenshtein_distance(s1,s2) == 0.7272727272727273
    True

    Damerau-Levenshtein Distance in Python _ Guy Rutenberg.htm
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

    return 1-float(float(d[lenstr1-1,lenstr2-1])/lengthmax)

if __name__ == '__main__':
    s1=input("Input text A:")
    s2=input("Input text B:")
    print("La subsecuencia mas larga con el metodo LCS es '%s'" % lcs(s1,s2))
    print("LCS distance:",longlcs(s1,s2))
    print("Damerau levenshtein distance:",damerau_levenshtein_distance(s1,s2))