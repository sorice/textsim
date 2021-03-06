#####!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Token Similarity Distances
==================================

Based on term/token similarity calculations.

"""

__author__ = 'Abel Meneses-Abad, Pablo Ulacia'

from ..decorators import string2tokenset, string2vec, string2qgrams

try:
    from nltk.metrics import jaccard_distance as jaccard_distance_nltk2
    from nltk.metrics import masi_distance as masi_distance_nltk
    from nltk.metrics import interval_distance as interval_distance_nltk
except:
    pass

try:
    from sklearn.metrics.pairwise import manhattan_distances as manhattan_distance_sklearn2
    from sklearn.metrics.pairwise import cosine_distances as cosine_distance_sklearn2
    from sklearn.metrics.pairwise import cosine_similarity as cosine_similarity_sklearn2
    from sklearn.metrics.pairwise import euclidean_distances as euclidean_distance_sklearn2
except:
    pass

try:
    from scipy.spatial.distance import braycurtis as braycurtis_scipy
    from scipy.spatial.distance import canberra as canberra_scipy
    from scipy.spatial.distance import chebyshev as chebyshev_scipy
    from scipy.spatial.distance import cityblock as cityblock_scipy
    from scipy.spatial.distance import correlation as correlation_scipy
    from scipy.spatial.distance import cosine as cosine_scipy
    from scipy.spatial.distance import dice as dice_scipy
    from scipy.spatial.distance import euclidean as euclidean_scipy
    from scipy.spatial.distance import hamming as hamming_scipy
    from scipy.spatial.distance import jaccard as jaccard_scipy
    from scipy.spatial.distance import kulsinski as kulsinski_scipy
    from scipy.spatial.distance import mahalanobis as mahalanobis_scipy
    from scipy.spatial.distance import matching as matching_scipy
    from scipy.spatial.distance import minkowski as minkowski_scipy
    from scipy.spatial.distance import rogerstanimoto as rogerstanimoto_scipy
    from scipy.spatial.distance import russellrao as russellrao_scipy
    from scipy.spatial.distance import seuclidean as seuclidean_scipy
    from scipy.spatial.distance import sokalmichener as sokalmichener_scipy
    from scipy.spatial.distance import sokalsneath as sokalsneath_scipy
    from scipy.spatial.distance import sqeuclidean as sqeuclidean_scipy
    from scipy.spatial.distance import yule as yule_scipy

except:
    pass

import numpy as np
from scipy.spatial.distance import _convert_to_double
from ..decorators import score_original, Appender

from .distances_doc import *

@string2tokenset
def jaccard_distance_textsim(s1,s2):
    """Textsim implementation of Jaccard or Tanimoto distance.
    """
    c1 = s1 & s2
    c2 = s1 | s2
    return float(abs(len(c1)-len(c2)))/(len(c2) or 1.0)

#from NLTK package if installed
@string2tokenset
@Appender(jaccard_distance_textsim.__doc__)
def jaccard_distance_nltk(s1,s2):
    """NLTK Jaccard distance implementation.
    """
    return jaccard_distance_nltk2(s1,s2)

@string2tokenset
@Appender(masi_doc)
def masi_distance(s1,s2):
    """NLTK Masi distance implementation.
    """
    return masi_distance_nltk(s1,s2)

@string2tokenset
@Appender(interval_doc)
def interval_distance(s1,s2):
    """NLTK Interval distance implementation.
    """
    return float(interval_distance_nltk(s1.__len__(),s2.__len__()))

#from Sklearn package if installed
@string2vec
@Appender(manhattan_dist_sklearn_doc)
def manhattan_distance_sklearn(s1,s2):
    """Sklearn implementation of Manhattan distance also known as City Block, L1.
    """
    return manhattan_distance_sklearn2(s1,s2)

@string2vec
@Appender(euclidean_dist_doc)
def euclidean_distance_sklearn(s1,s2):
    """Sklearn implementation of Euclidean distance also known as L2.
    """
    return euclidean_distance_sklearn2(s1,s2)

@string2vec
@Appender(cosine_dist_sklearn_doc)
def cosine_distance_sklearn(s1,s2):
    """Sklearn implementation of Cosine distance.
    """
    return cosine_distance_sklearn2(s1,s2)

@string2vec
@Appender(cosine_similarity_sklearn_doc)
def cosine_similarity_sklearn(s1,s2):
    """Sklearn implementation of Cosine similarity also known as Orchini, Angular, Niche.
    """
    return cosine_similarity_sklearn2(s1,s2)

#from Scipy package if installed
@string2vec
@Appender(braycurtis_scipy.__doc__)
def braycurtis_distance_scipy(s1,s2):
    ""
    return braycurtis_scipy(s1,s2)

@string2vec
@Appender(canberra_scipy.__doc__)
def canberra_distance_scipy(s1,s2):
    ""
    return canberra_scipy(s1,s2)

@string2vec
@Appender(chebyshev_scipy.__doc__)
def chebyshev_distance_scipy(s1,s2):
    ""
    return chebyshev_scipy(s1,s2)

@string2vec
@Appender(cityblock_scipy.__doc__)
def cityblock_distance_scipy(s1,s2):
    ""
    return cityblock_scipy(s1,s2)

@string2vec
@Appender(correlation_scipy.__doc__)
def correlation_distance_scipy(s1,s2):
    ""
    return correlation_scipy(s1,s2)

@string2vec
@Appender(cosine_scipy.__doc__)
def cosine_distance_scipy(s1,s2):
    ""
    return 1-cosine_scipy(s1,s2)

@string2vec
@Appender(dice_scipy.__doc__)
def dice_distance_scipy(s1,s2):
    ""
    return dice_scipy(s1,s2)

@string2vec
@Appender(euclidean_scipy.__doc__)
def euclidean_distance_scipy(s1,s2):
    ""
    return euclidean_scipy(s1,s2)

@string2vec
@Appender(hamming_scipy.__doc__)
def hamming_distance_scipy(s1,s2):
    ""
    return hamming_scipy(s1,s2)

@string2vec
@Appender(jaccard_scipy.__doc__)
def jaccard_distance_scipy(s1,s2):
    ""
    return 1-jaccard_scipy(s1,s2)

@string2vec
@Appender(kulsinski_scipy.__doc__)
def kulsinski_distance_scipy(s1,s2):
    ""
    return kulsinski_scipy(s1,s2)

@string2vec
@Appender(mahalanobis_scipy.__doc__)
def mahalanobis_distance_scipy(s1,s2):
    ""
    [XA] = _convert_to_double(s1)
    [XB] = _convert_to_double(s2)
    X = np.vstack([XA, XB])
    VI = np.cov(X.T)
    return mahalanobis_scipy(s1,s2,VI)

@string2vec
@Appender(matching_scipy.__doc__)
def matching_distance_scipy(s1,s2):
    ""
    return matching_scipy(s1,s2)

@string2vec
@Appender(minkowski_scipy.__doc__)
def minkowski_distance_scipy(s1,s2):
    ""
    return minkowski_scipy(s1,s2, p=1)

@string2vec
@Appender(rogerstanimoto_scipy.__doc__)
def rogerstanimoto_distance_scipy(s1,s2):
    ""
    try:
        score = rogerstanimoto_scipy(s1,s2)
        return score
    except: 
        return 0.0

@string2vec
@Appender(russellrao_scipy.__doc__)
def russellrao_distance_scipy(s1,s2):
    ""
    return russellrao_scipy(s1,s2)

@string2vec
@Appender(seuclidean_scipy.__doc__)
def seuclidean_distance_scipy(s1,s2):
    ""
    [XA] = _convert_to_double(s1)
    [XB] = _convert_to_double(s2)
    X = np.vstack([XA, XB])
    V = np.var(X, axis=0, ddof=1)
    for i,e in enumerate(V):
        if e == 0.0:
            V[i] = V.mean()
    return np.sqrt(((XA - XB) ** 2 / V).sum())

@string2vec
@Appender(sokalmichener_scipy.__doc__)
def sokalmichener_distance_scipy(s1,s2):
    ""
    try:
        score = sokalmichener_scipy(s1,s2)
        return score
    except:
        return 0.0

@string2vec
@Appender(sokalsneath_scipy.__doc__)
def sokalsneath_distance_scipy(s1,s2):
    ""
    try:
        score = sokalsneath_scipy(s1,s2)
        return score
    except:
        return 0.0

@string2vec
@Appender(sqeuclidean_scipy.__doc__)
def sqeuclidean_distance_scipy(s1,s2):
    ""
    return sqeuclidean_scipy(s1,s2)

@string2vec
@Appender(yule_scipy.__doc__)
def yule_distance_scipy(s1,s2):
    ""
    return yule_scipy(s1,s2)

#Textsim self tokendists implementations
@string2tokenset
@Appender(matching_coefficient_doc)
def matching_coefficient_textsim(s1,s2):
    """
    Textsim implementation of Matching Coefficient.
    """
    return float(len(s1.union(s2)))

@string2tokenset
@Appender(dice_coefficient_doc)
def dice_coefficient_textsim(s1,s2):
    """
    Textsim implementation of Dice Coefficient.
    """
    c1 = s1 & s2
    c2 = s1 | s2
    return 2*(float(len(c1)))/(float(len(c1)+len(c2)) or 1.0)

@string2tokenset
@Appender(overlap_distance_doc)
def overlap_distance_textsim(s1,s2):
    """
    Textsim Overlap distance implementation.
    """
    return float(len(s1.intersection(s2)))/(float(min(len(s1),len(s2))) or 1.0)

@string2tokenset
@Appender(matching_coefficient_pablo_doc)
def matching_coefficient_pablo(s1,s2):
    """
    Pablo Ulacia variation of matching coefficient, procedence of the original
    formula remains unknown.
    """
    return float(len(s1)-len(s1.intersection(s2)))/(max(len(s1),len(s2)) or 1.0)

@string2tokenset
@Appender(containment_distance_doc)
def containment_distance(s1, s2):
    """Textsim implementation of Containment Similarity token-based.
    """
    return len(s1 & s2) / (float(len(s1)) or 1.0)

@string2qgrams
@Appender(qgram_distance_doc)
def qgram_distance(s1, s2, **param):
    """Textsim implementation of Q-gram Similarity distance.
    """
    if 'method' in param and param['method'] == 'overlap':
        return len(set(s1).intersection(set(s2))) / (float(len(set(s1))) or 1.0)
    else:
        return 2*len(set(s1).intersection(set(s2))) / (float(len(set(s1))+len(set(s2))) or 1.0)

if __name__ == '__main__':
        v1="PCCW's chief operating officer, Mike Butcher, and Alex Arena, the chief financial officer, will report directly to Mr So."
        v2="Current Chief Operating Officer Mike Butcher and Group Chief Financial Officer Alex Arena will report to So."
        print("MASI distance:", masi_distance_nltk("0.1 0.2 0.3 0.4", "0.1 0.2 0.3 0.5"))
        print("Dice's coefficient:",dice_coefficient_textsim(v1,v2))
        print("Matching coefficient:",matching_coefficient_textsim("0.1 0.2 0.3 0.4","0.1 0.2 0.3 0.5"))
        print("Jaccard:",jaccard_distance(v1,v2))
        print("Overlap coefficient:",overlap("0.1 0.2 0.3 0.4","0.1 0.2 0.3 0.5"))
        print("Cosine distance:",cosine_distance("0.1 0.2 0.3 0.4","0.1 0.2 0.3 0.5"))
        print("Euclidean distance:",euclidean_distance(v1,v2))
        print("Manhattan distance:",manhattan_distance(v1,v2))

