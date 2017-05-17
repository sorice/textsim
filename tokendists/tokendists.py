#####!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Token Similarity Distances
==================================

Based on term/token similarity calculations.

"""

__author__ = 'Abel Meneses-Abad, Pablo Ulacia'

from ..decorators import string2tokenset, string2vec

try:
    from nltk.metrics import jaccard_distance as jaccard_distance_nltk
    from nltk.metrics import masi_distance as masi_distance_nltk
    from nltk.metrics import interval_distance as interval_distance_nltk
except:
    pass

try:
    from sklearn.metrics.pairwise import manhattan_distances as manhattan_sklearn
    from sklearn.metrics.pairwise import cosine_distances as cosine_distance_sklearn
    from sklearn.metrics.pairwise import euclidean_distances as euclidean_distances_sklearn
except:
    pass

try:
    from scipy.spatial.distance import jaccard as jaccard_scipy
except:
    pass

@string2tokenset
def jaccard_distance(s1,s2):
    return jaccard_distance_nltk(s1,s2)

@string2vec
def manhattan_distance(s1,s2):
    "Manhattan distance also known as City Block, L1. "
    return manhattan_sklearn(s1,s2)

@string2vec
def euclidean_distance(s1,s2):
    "Euclidean distance also known as L1. "
    return euclidean_distances_sklearn(s1,s2)

@string2vec
def cosine_distance(s1,s2):
    "Cosine distance also known as Orchini, Angular, Niche."
    return cosine_distance_sklearn(s1,s2)

@string2vec
def jaccard_distance_scipy(s1,s2):
    "Jaccard distance also known as Tanimoto distance."
    return jaccard_scipy(s1,s2)

@string2tokenset
def masi_distance(s1,s2):
    "Masi distance "
    return masi_distance_nltk(s1,s2)

@string2tokenset
def interval_distance(s1,s2):
    "Interval distance."
    return interval_distance_nltk(s1.__len__(),s2.__len__())

@string2tokenset
def matching_coefficient(s1,s2):
    """
    Medida de similitud basada en vectores. Similar a la distancia de Hamming pero
    esta debe ser entre vectores de igual longitud. Esta distancia va a devolver un
    valor entre [0-x] donde cuanto menor sea la distancia entre los vectores mas
    semejanza existira por lo que su valor tendera a 0.
    En esta implementacion se realizo una modificacion para obtener un valor entre [0-1]
    donde cuando tiende a 1 es que existe mayor similitud y cuando tiende a 0 tiene menor
    similitud.
    Esta operacion se realizo dividiendo entre la longitud de la cadena mas larga y restando el resultado
    con 1 para invertir el orden a que esta tendiendo

                   (|x|-|x∩y|)
    M(x,y) = 1 -  -----------------
                   max_longitud(x,y)

    @param s1, s2: Cadenas a analizar
    @type s1: str
    @type s2: str
    @rtype: float

    >>> x = "0.1 0.2 0.3 0.4"
    >>> y = "0.1 0.2 0.3 0.5"
    >>> idioma = 'english'
    >>> matching_coefficient(x, y, "", "",idioma) ==  0.75
    True

    Understanding Plagiarism Linguistic Patterns,Textual Features, and Detection Methods
    Salha M. Alzahrani, Naomie Salim, and Ajith Abraham, Senior Member, IEEE
    """
    maxlen = float(max(len(s1),len(s2)))
    return 1-(maxlen -len(s1.intersection(s2)))/maxlen

@string2tokenset
def jaccard_distance_textsim(s1,s2):
    """
    Jaccard or Tanimoto distance.
    La medida de Jaccard es una medida de similitud que va a tender a 1 mientras mas
    semejanza exista entre dos vectores y el rango de su resultado va estar entre [0-1]

                    |X ∩ Y|
    jaccard(X,Y) = -----------
                    |X ∪ Y|

    @param s1, s2: Cadenas a analizar
    @type s1: str
    @type s2: str
    @rtype: float

    >>> x = "0.1 0.2 0.3 0.4"
    >>> y = "0.1 0.2 0.3 0.5"
    >>> idioma = 'english'
    >>> jaccard(x, y, "", "",idioma) == 0.6
    True
    Understanding Plagiarism Linguistic Patterns,Textual Features, and Detection Methods
    Salha M. Alzahrani, Naomie Salim, and Ajith Abraham, Senior Member, IEEE
    """
    c1 = s1 & s2
    c2 = s1 | s2
    if len(c2) == 0:
        result = 'inf'
    else:
        result = float(abs(len(c1)-len(c2)))/len(c2)
    return result

@string2tokenset
def dice_coefficient_textsim(s1,s2):
    """
    La medida de Dice_coefficient (similar a Jaccard) es una medida de similitud que va
    a tender a 2 mientras mas semejanza exista entre dos vectores y el rango de su
    resultado va estar entre [0-2]

                    2|X ∩ Y|
    dice(X,Y) = -----------
                     |X|+|Y|

    @param s1, s2: Cadenas a analizar
    @type s1: str
    @type s2: str
    @rtype: float

    >>> x = "0.1 0.2 0.3 0.4"
    >>> y = "0.1 0.2 0.3 0.5"
    >>> idioma = 'english'
    >>> dice_coefficient(x, y, "", "",idioma) == 1.2
    True

    Understanding Plagiarism Linguistic Patterns,Textual Features, and Detection Methods
    Salha M. Alzahrani, Naomie Salim, and Ajith Abraham, Senior Member, IEEE
    """
    c1 = s1 & s2
    c2 = s1 | s2
    return 2*(float(len(c1)))/(float(len(c2))+float(len(c2)))

@string2tokenset
def overlap_distance_textsim(s1,s2):
    """
    Overlap es una medida que tiende a 1 mientras mayor sea la semejanza entre los
    dos vectores y su resultado esta entre [0-1]. Este machea completamente si el vector1
    es un subconjunto del vector2 o viceversa

                |X ∩ Y|
    OC(x,y)= ---------------
              min(|x|,|y|)

    @param s1, s2: Cadenas a analizar
    @type s1: str
    @type s2: str
    @rtype: float

    >>> x = "0.1 0.2 0.3 0.4"
    >>> y = "0.1 0.2 0.3 0.5"
    >>> idioma = 'english'
    >>> overlap(x, y, "", "", idioma) == 0.75
    True

    Understanding Plagiarism Linguistic Patterns,Textual Features, and Detection Methods
    Salha M. Alzahrani, Naomie Salim, and Ajith Abraham, Senior Member, IEEE
    """

    if float(min(len(s1),len(s2))) == 0:
        result = 'inf'
    else:
        result = float(len(s1.intersection(s2)))/float(min(len(s1),len(s2)))

    return result

@string2tokenset
def euclidean_distance_textsim(s1,s2):
    """
    Euclidean es una medida de distancia geometrica entre dos vectores que tiende a 0 mientras mas
    semejantes son los vectores. Esta medida utiliza el metodo tf para asignarle un peso a las palabras
    de acuerdo a la frecuencia.
    En esta implementacion se realizo una modificacion para obtener un valor entre [0-1]
    donde cuando tiende a 1 es que existe mayor similitud y cuando tiende a 0 tiene menor
    similitud.
    Esta operacion se realizo  restando el resultado con 1 para invertir el orden a que esta tendiendo

                               ₂
    euclidean(x,y)= ⎷∑ |x - y |
                      i  i   i

    @param s1, s2: Cadenas a analizar
    @type s1: str
    @type s2: str
    @rtype: float

    >>> x = "0.1 0.2 0.3 0.4"
    >>> y = "0.1 0.2 0.3 0.5"
    >>> idioma = 'english'
    >>> euclidean(x, y, "", "", idioma) == 1.0
    True

    Understanding Plagiarism Linguistic Patterns,Textual Features, and Detection Methods
    Salha M. Alzahrani, Naomie Salim, and Ajith Abraham, Senior Member, IEEE
    """

    s1 = list(s1)
    s2 = list(s2)

    suma=0
    if len(s1)<len(s2):
        for i in range(len(s1)):
            suma+=pow(tf(s1[i],s1) - tf(s2[i],s2),2)
        return float(1-float(pow(suma,0.5)))
    else:
        for i in range(len(s2)):
            suma+=pow(tf(s1[i],s1) - tf(s2[i],s2),2)
        return float(1-float(pow(suma,0.5)))

def tf(t,d):
    return float(d.count(t)) / float(sum(d.count(w) for w in set(d)))

@string2tokenset
def jaccard_ulacia(s1,s2):
    """Modificacion de la medida Jaccard utilizando wordnet para expandir la busqueda

    @param s1, s2: Cadenas a analizar
    @type s1: str
    @type s2: str
    @rtype: float

    >>> import nltk
    >>> from nltk.tokenize import word_tokenize
    >>> from nltk.corpus import stopwords
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
                    tmp=float(damerau_levenshtein_distance(i, j, doc1, doc2))
                else:
                    tmp=float(damerau_levenshtein_distance(i, j, doc1, doc2))
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
        print("Binary distance:", binary_distance("0.1 0.2 0.3 0.4", "0.1 0.2 0.3 0.5"))
        print("MASI distance:", masi_distance("0.1 0.2 0.3 0.4", "0.1 0.2 0.3 0.5"))
        print("Dice's coefficient:",dice_coefficient(v1,v2))
        print("Matching coefficient:",matching_coefficient("0.1 0.2 0.3 0.4","0.1 0.2 0.3 0.5"))
        print("Jaccard:",jaccard(v1,v2))
        print("Overlap coefficient:",overlap("0.1 0.2 0.3 0.4","0.1 0.2 0.3 0.5"))
        print("Cosine distance:",cos("0.1 0.2 0.3 0.4","0.1 0.2 0.3 0.5"))
        print("Euclidean distance:",euclidean(v1,v2))
        print("Manhattan distance:",manhattan(v1,v2))
        print("jaccard_ulacia distance:",jaccard_ulacia(v1,v2))
