#####!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Complementary documentation for distances
============================================

Textsim package additional documentation for distance's doc normalization.

"""

jaccard_doc = """
    The Jaccard distance tends to 1 while compared vectors are more similar.
    The range of values is between [0-1] [Jaccard1901]_.

    .. math::

        jaccard(X,Y) = \\frac{|X ∩ Y|}{|X ∪ Y|}


    where :math:`X` and :math:`Y` are the token set of each sentence :math:`s1,s2`
    respectively.

    :Citation:

    .. [Jaccard1901] Jaccard, P. (1901). Étude comparative de la distribution
        florale dans une portion des Alpes et des Jura. Bulletin de la Société
        Vaudoise des Sciences Naturelles 37, 547-579.

    :param s1,s2: Sentences to compare.
    :type s1,s2: str
    :returns: float

    :Examples:

    >>> x = "0.1 0.2 0.3 0.4"
    >>> y = "0.1 0.2 0.3 0.5"
    >>> jaccard(x, y) == 0.6
    True

    """


masi_doc = """
    Distance metric that takes into account partial agreement when multiple
    labels are assigned [Passonneau2006]_.

    .. math::

        masi(X,Y) = 1 - \\frac{|X ∩ Y|}{|X ∪ Y|*m}

    where :math:`X` and :math:`Y` are the token set of each sentence :math:`s1,s2`
    respectively and:

        * :math:`m = 1` if :math:`|X ∩ Y| = |X| = |Y|`
        * :math:`m = 0.67` if :math:`|X ∩ Y| = min(|X|,|Y|)`
        * :math:`m = 0.33` if :math:`|X ∩ Y| > 0`
        * :math:`m = 0` if :math:`|X ∩ Y| = 0`

    :Citation:

    ..  [Passonneau2006] Measuring Agreement on Set-Valued Items (MASI)
        for Semantic and Pragmatic Annotation. 2006.

    :param s1,s2: Sentences to compare.
    :type s1,s2: str
    :rtype: float

    :Examples:

    >>> from nltk.metrics import masi_distance
    >>> masi_distance(set([1, 2]), set([1, 2, 3, 4]))
    0.665...

    """

interval_doc = """
    Krippendorff's interval distance metric [Krippendorff1980]_.

    .. math::

        interval(X,Y) = (|X - |X ∩ Y||)^2

    where :math:`X` and :math:`Y` are the token set of each sentence :math:`s1,s2`
    respectively.

    :Citation:

    ..  [Krippendorff1980] Krippendorff 1980. Content Analysis: An Introduction to
         its Methodology

    :param s1,s2: Sentences to compare.
    :type s1,s2: str
    :rtype: float

    :Examples:

    >>> from nltk.metrics import interval_distance
    >>> interval_distance(1,10)
    81

    """

#Here it is possible to construct complex refactorizations of original doc
#from external functions. E.g. interval_distance_nltk actual (2017) structure =
# title, doctest, reference
# final structure in textsim package = title, %s, %s, %s, %s doctest %
#                (:explanation:, :math:, :brief formula explanation:, reference)

# Another example: chebyshev in scipy package
# actual structure = title, explanation, math, parameters, returns
# textsim_structure = title, explanation, math, :brief formula explanation:
#                       parameters, returns, ref

# sklearn example: euclidean_distances
# actual structure = explanation, unformat math, more explanation, parameters
#                   returns, example, see also
# textsim_structure =
    # (%s, explanation, %s-re, %s, parameters, returns, %s-re, %s, see also)  %
    # (title,formated math, :brief formula explanation:, example as doctest, ref)

manhattan_dist_sklearn_doc = """
    Compute the L1 distances between the vectors in X and Y.

    With sum_over_features equal to False it returns the componentwise
    distances. The :math:`L_1` or block distance is calcualted from summing
    the edge distances [Krause1973]_.

    .. math::

        L_1(X,Y) = \\sum_{i} |X_i-Y_i|

    where :math:`X` and :math:`Y` are the term frecuency vector of each
    sentence :math:`s1,s2` respectively.

    :Internal Formula Explanation:

    :param X: An array with shape (n_samples_X, n_features).
    :type X: array_like
    :param Y: An array with shape (n_samples_Y, n_features).
    :type Y: array_like, optional
    :param sum_over_features: If True the function returns the pairwise
        distance matrix else it returns the componentwise L1 pairwise-distances.
        Not supported for sparse matrix inputs.
    :type sum_over_features: bool, default=True
    :param size_threshold: Unused parameter.
    :type size_threshold: int, default=5e8
    :returns:
        * D: If sum_over_features is False shape is
        (n_samples_X * n_samples_Y, n_features) and D contains the
        componentwise L1 pairwise-distances (ie. absolute difference),

        * else shape is (n_samples_X, n_samples_Y) and D contains
        the pairwise L1 distances.
    :rtype: array

    :Citation:

    .. [Krause1973] Eugene F. Krause. (1973). Taxicab Geometry, Dover.
       The Mathematics Teacher, 66(8):695-706. JSTOR publisher.
       ISBN: 0-486-25202-7.

    :param s1,s2: Sentences to compare.
    :type s1,s2: str
    :rtype: float

    :Examples:

    >>> from sklearn.metrics.pairwise import manhattan_distances
    >>> manhattan_distances([[3]], [[3]])#doctest:+ELLIPSIS
    array([[ 0.]])
    >>> manhattan_distances([[3]], [[2]])#doctest:+ELLIPSIS
    array([[ 1.]])
    >>> manhattan_distances([[2]], [[3]])#doctest:+ELLIPSIS
    array([[ 1.]])
    >>> manhattan_distances([[1, 2], [3, 4]],\
         [[1, 2], [0, 3]])#doctest:+ELLIPSIS
    array([[ 0.,  2.],
           [ 4.,  4.]])
    >>> import numpy as np
    >>> X = np.ones((1, 2))
    >>> y = 2 * np.ones((2, 2))
    >>> manhattan_distances(X, y, sum_over_features=False)#doctest:+ELLIPSIS
    array([[ 1.,  1.],
           [ 1.,  1.]]...)

    :See also:

    Read more in the **Sklearn User Guide** :mod:`metrics`.

    """

euclidean_dist_doc ="""Computes the paired euclidean distances between X and Y.

    Considering the rows of X (and Y=X) as vectors, compute the
    distance matrix between each pair of vectors.[Deza2009]_

    For efficiency reasons, the euclidean distance between a pair of row
    vector x and y is computed as:

    .. math::

        L_2(X, Y) = \sqrt(\sum_{i} (X_i - Y_i)^2)


    where :math:`X` and :math:`Y` are the term frecuency vector of each
    sentence :math:`s1,s2` respectively.

    Optimized equation for computing:

    .. math::

        dist(X, Y) = sqrt(dot(X, X) - 2 * dot(X, Y) + dot(Y, Y))

    :Additional Sklearn Formula Explanation:

    :param X: {array-like, sparse matrix}, shape (n_samples_1, n_features)
    :param Y: : {array-like, sparse matrix}, shape (n_samples_2, n_features)
    :param Y_norm_squared: optional, pre-computed dot-product of vectors in Y.
    :type Y_norm_squared: array-like, shape (n_samples_2, )
    :param squared : boolean, optional
    :param X_norm_squared: optional, pre-computed dot-product of vectors in X.
    :type X_norm_squared: array-like, shape = [n_samples_1]
    :returns: Return squared Euclidean distances.
    :rtype: distances : {array, sparse matrix}, shape (n_samples_1, n_samples_2)

    .. note::

        pre-computed dot-products of vectors in Y = ``(Y**2).sum(axis=1)``

    This formulation has two advantages over other ways of computing distances.
    First, it is computationally efficient when dealing with sparse data.
    Second, if one argument varies but the other remains unchanged, then
    `dot(x, x)` and/or `dot(y, y)` can be pre-computed.

    However, this is not the most precise way of doing this computation, and
    the distance matrix returned by this function may not be exactly
    symmetric as required by, e.g., ``scipy.spatial.distance`` functions.

    :Citation:

    .. [Deza2009] Michel María Daeza and Elena Daeza.
        Encyclopedia of Distances.
        Springer-Verlag Berlin Heidelberg, 2009.
        ISBN: 978-3-642-00233-5

    :param s1,s2: Sentences to compare.
    :type s1,s2: str
    :rtype: float

    :Examples:

    >>> from sklearn.metrics.pairwise import euclidean_distances
    >>> X = [[0, 1], [1, 1]]
    >>> # distance between rows of X
    >>> euclidean_distances(X, X)
    array([[ 0.,  1.],
           [ 1.,  0.]])
    >>> # get distance to origin
    >>> euclidean_distances(X, [[0, 0]])
    array([[ 1.        ],
           [ 1.41421356]])

    :See also:

    Read more in the **Sklearn User Guide** :mod:`metrics`.
    paired_distances : distances betweens pairs of elements of X and Y.
    """

cosine_dist_sklearn_doc ="""Compute cosine distance between samples in X and Y.

    Cosine distance is defined as 1.0 minus the cosine similarity [Salton1975]_.

    .. math::

        d_{cos}(X,Y) = 1 - cosine_similarity

    Where :math:`X` and :math:`Y` are the term frecuency vector of each
    sentence :math:`s1,s2` respectively.

    :Internal Formula Explanation:

    :param X: array_like, sparse matrix with shape (n_samples_X, n_features).
    :param Y: array_like, sparse matrix (optional) with shape
            (n_samples_Y, n_features).
    :returns: distance matrix : An array with shape (n_samples_X, n_samples_Y).
    :rtype: array

    :Citation:

    .. [Salton1975] Salton, G.; Wong, A. & Yang, C. S.
        A Vector Space Model for Automatic Indexing Commun ACM,18(11):1-32.
        ACM, 1975.

    :param s1,s2: Sentences to compare.
    :type s1,s2: str
    :rtype: float

    :Examples:

    >>>from sklearn.metrics.pairwise import cosine_distances
    >>>from sklearn.feature_extraction.text import CountVectorizer
    >>>s1 = "PCCW's chief operating officer, Mike Butcher, and Alex Arena"
    >>>s2 = "Current Chief Operating Officer Mike Butcher and Group Chief"
    >>>countv = CountVectorizer()
    >>>tdm = countv.fit_transform([s1,s2])
    >>>X,Y = tdm[0],tdm[1]
    >>>float(cosine_distances(X,Y))
    0.296...

    >>>from textsim.tokendists import cosine_distance_sklearn
    >>>cosine_distance_sklearn(s1,s2)
    0.296...

    :See also:

    scipy.spatial.distance.cosine (dense matrices only)
    Read more in the **Sklearn User Guide** :mod:`metrics`.

    """

cosine_similarity_sklearn_doc = """
Cosine similarity is a vector based similarity measure. Input strings are
transformed into vector space (in a Term Frecuency model), then the Euclidean
cosine rule can be used to calculate the similarity [Deza2009]_.

.. math::

    cos(X,Y) = \\frac{\\sum_i{(x_i*y_i)}}{\sqrt{\\sum x_i^2* \\sum y_i^2}}

:Math Algebra Notation:

.. math::

    cos(X,Y) = \\frac{<X,Y>}{||X||*||Y||}

Where :math:`X` and :math:`Y` are the term frecuency vector of each
sentence :math:`s1,s2` respectively, and :math:`[x_1,...,x_{n}]` is the
representation of X based on the frecuencies of terms contained in the
union of the token set representations of s1 and s2 (:math:`s1 ∪ s2`). Ibidem
for :math:`Y = [y_1,...,y_{n}]`.

:Internal Formula Explanation:

:param X: ndarray or sparse array, shape: (n_samples_X, n_features)
:param Y: ndarray or sparse array, shape: (n_samples_Y, n_features)
        Input data. If ``None``, the output will be the pairwise
        similarities between all samples in ``X``.
:param dense_output: boolean (optional), default True
        Whether to return dense output even when the input is sparse. If
        ``False``, the output is sparse if both input arrays are sparse.
:returns kernel matrix: An array with shape (n_samples_X, n_samples_Y).

:Citation:

.. [Deza2009] Michel María Daeza and Elena Daeza.
    Encyclopedia of Distances.
    Springer-Verlag Berlin Heidelberg, 2009.
    ISBN: 978-3-642-00233-5

param s1,s2: Sentences to compare.
:type s1,s2: str
:rtype: float

:Examples:

>>>from textsim.tokendists import cosine_distance_sklearn
>>>s1 = "PCCW's chief operating officer, Mike Butcher, and Alex Arena"
>>>s2 = "Current Chief Operating Officer Mike Butcher and Group Chief"
>>>cosine_similarity_sklearn(s1,s2)
0.703...

:See also:

Read about *Text Feature Extraction* in the **Sklearn User Guide**
:mod:`feature_extraction`.

"""

dice_coefficient_doc = """
Returns the similarity between string1 and string1 as a number between [0,1]
based on the number of shared tokens [dice1945]_.

.. math::

    dice(X,Y) = \\frac{2*|X ∩ Y|}{|X|+|Y|}


where :math:`X` and :math:`Y` are the token set of each sentence :math:`s1,s2`
respectively.

:Citation:

.. [dice1945] Lee R. Dice (1945).
    Measures of the amount of ecologic association between species.
    Journal of Ecology 26(3): 297-302. Wiley Online Library

:param s1, s2: The strings to be analysed
:type s1: str
:type s2: str
:rtype: float

:Examples:

>>> from textsim.tokendists import dice_coefficient_textsim
>>> s1 = "PCCW's chief operating officer, Mike Butcher, and Alex Arena"
>>> s2 = "Current Chief Operating Officer Mike Butcher and Group Chief"
>>> dice_coefficient_textsim(s1,s2)
0.307...
"""

overlap_distance_doc = """
Overlap coefficient considers two strings a full match if one is a subset of
another and it is similar to Dice Coefficient. The overlap coefficient also
called as Szymkiewicz-Simpson coefficient is a similarity measure that is
related to the Jaccard index. It measures the overlap between two sets.
The measure is calculated by dividing the size of the intersection by the
smaller of the size of the two sets [simpson1960]_,[Vijaymeena2016]_.

.. math::

    OC(X,Y) = \\frac{|X ∩ Y|}{min(|X|,|Y|)}

where :math:`X` and :math:`Y` are the token set of each sentence :math:`s1,s2`
respectively.

:Citation:

.. [simpson1960] George Gaylord Simpson (1960).
    Notes on the measurement of faunal resemblance.
    American Journal of Science, 1960, 258(2): 300-311.

.. [Vijaymeena2016] M.K. Vijaymeena & K. Kavitha (2016).
    A SURVEY ON SIMILARITY MEASURES IN TEXT MINING
    Machine Learning and Applications: An International Journal (MLAIJ), 3, 19-28.

:param s1, s2: The strings to be analysed
:type s1: str
:type s2: str
:rtype: float

:Examples:

>>> from textsim.tokendists import overlap_distance_textsim
>>> x = "0.1 0.2 0.3 0.4"
>>> y = "0.1 0.2 0.3 0.5"
>>> overlap_distance_textsim(x, y) == 0.75
True

TODO: ngrams generalization

"""

matching_coefficient_doc = """
The Matching Coefficient is a very simple vector based approach which simply
counts the number of terms, (dimensions), on which both vectors are non zero.
This is similar to the vector version of the simple hamming distance
although position is not taken into account []_,[]_.

.. math::

    match_{coefficients}(X,Y) = |X ∩ Y|

where :math:`X` and :math:`Y` are the token set of each sentence :math:`s1,s2`
respectively.

:Citation:

.. [Sokal1985] RR Sokal (1985).
    The principles of numerical taxonomy: twenty-five years later.
    Computer-assisted bacterial systematics (15). Academic Press.


:param s1, s2: The strings to be analysed
:type s1: str
:type s2: str
:rtype: float

:Examples:

>>> from textsim.tokendists import matching_coefficient_textsim
>>> s1 = "PCCW's chief operating officer, Mike Butcher, and Alex Arena"
>>> s2 = "Current Chief Operating Officer Mike Butcher and Group Chief"
>>> matching_coefficient_textsim(s1,s2)
13.0

TODO: ngrams generalization

"""

matching_coefficient_pablo_doc = """
Variation of matching coefficients [Alzahrani2012]_ presented by Pablo Ulacia
in [Ulacia2016]_.

.. math::

    M(X,Y) = \\frac{|x|-|x∩y|}{max_length(x,y)}

where :math:`X` and :math:`Y` are the token set of each sentence :math:`s1,s2`
respectively.

:Citation:

.. [Ulacia2016] Pablo Ulacia Villavicencio (2016).
    Biblioteca de medidas de similitud para textos.
    Bachelor of Computational Science, UCLV, Cuba.

.. [Alzahrani2012] Alzahrani, S. M.; Salim, N. & Abraham, A (2012).
    Understanding Plagiarism Linguistic Patterns, Textual Features, and
    Detection Methods. IEEE Trasactions on systems, man and Cibernetics 42:
    133-149. IEEE.

:param s1, s2: The strings to be analysed
:type s1: str
:type s2: str
:rtype: float

:Examples:

>>> X = "0.1 0.2 0.3 0.4"
>>> Y = "0.1 0.2 0.3 0.5"
>>> idioma = 'english'
>>> matching_coefficient_pablo(X,Y) ==  0.75
True

TODO: ngrams generalization

"""

containment_distance_doc = """
Similar to the Jaccard coefficient, the containment measure calculates the
intersection of elements between both strings but normalises them only with
respect to the elements in the suspicious string. Commonly used in text reuse
field to calculate similarity between documents.

.. math::

    containment(X,Y) = \\frac{|X ∩ Y|}{|X|}

where :math:`X` and :math:`Y` are the token set of each sentence :math:`s1,s2`
respectively.

:Citation:

.. [Broader1997] Andrei Z. Broder (1997).
    On the Resemblance and Containment of Documents.
    In Compression and Complexity of Sequences (SEQUENCES’97), pages 21–29.
    IEEE Computer Society.

:param s1, s2: The strings to be analysed
:type s1: str
:type s2: str
:rtype: float

:Examples:

>>> from textsim.tokendists import containment_similarity_textsim
>>> s1 = "PCCW's chief operating officer, Mike Butcher, and Alex Arena"
>>> s2 = "Current Chief Operating Officer Mike Butcher and Group Chief"
>>> containment_similarity_textsim(s1,s2)
0.444...

:See also:

textsim.jaccard

TODO: ngrams generalization

"""

greedy_string_tiling_doc = """
When comparing two strings A and B, the aim is to find a maximal set of
contiguous substrings that have the following properties: each substring occurs
in both A and B, is as long as possible and does not cover a token already
covered by some other substring. To avoid spurious matches, a minimum match
length M is enforced [Wise1993]_, [Wise1996]_.

.. math::

    D()

where :math:`X` and :math:`Y` are the token set of each sentence :math:`s1,s2`
respectively.

:Citation:

.. [Wise1993] Michael J. Wise. String similarity via greedy string tiling and
    running Karp-Rabin matching. ftp://ftp.cs.su.oz.au/michaelw/doc/RKR GST.ps,
    Dept. of CS, University of Sydney, December 1993.

.. [Wise1996] Michael J. Wise (1996).
   YAP3: Improved detection of similarities in computer program and other texts.
   ACM SIGCSE Bulletin, 28(1): 130-134. ACM.

:param s1, s2: The strings to be analysed
:type s1: str
:type s2: str
:rtype: float

:Examples:

>>> from textsim.tokendists import greedy_string_tiling
>>> s1 = "PCCW's chief operating officer, Mike Butcher, and Alex Arena"
>>> s2 = "Current Chief Operating Officer Mike Butcher and Group Chief"
>>> greedy_string_tiling(s1,s2)

TOD: implement this measure

"""

qgram_distance_doc = """
Qgrams are the sub-sets of Q-continuoum tokens in a sentence. E.g. the
bigrams of the sentence 'Jonh eat fish' are (Jonh,eat) and (eat,fish).
This kind of representation is very useful for probabilistic models
like Hiden Markov Models.

.. math::

    qgram(X,Y) = {2*|q(X) ∩ q(Y)| \over |q(X)|+|q(Y)|}

Where :math:`q(X),q(Y)` and :math:`q(X,Y)` are the sizes of multisets of
all q-grams (sub-sets of tokens of length q) occurring in X, Y and both
of them, respectively.

:Citation:

.. [ukkonen1992] Esko Ukkonen (1992).
    Approximate string-matching with q-grams and maximal matches.
    In Theoretical computer science (92) 1, pages 191-211.
    Elsevier.

:param s1, s2: The strings to be analysed
:type s1: str
:type s2: str
:rtype: float

:Examples:

>>> from textsim.tokendists import qgram_distance
>>> s1 = "PCCW's chief operating officer, Mike Butcher, and Alex Arena"
>>> s2 = "Current Chief Operating Officer Mike Butcher and Group Chief"
>>> qgram_distance(s1,s2)

"""
