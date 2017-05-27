#####!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Complementary documentation for distances
============================================

Textsim package additional documentation for distance's doc normalization.

"""

jaccard_doc = """The Jaccard distance tends to 1 while compared vectors are more similar.
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

    :Doctest:

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
        for Semantic and Pragmatic Annotation.

    :param s1,s2: Sentences to compare.
    :type s1,s2: str
    :rtype: float

    :Doctest:

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

    :Doctest:

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

manhattan_dist_sklearn_doc = """Compute the L1 distances between the vectors in X and Y.

    With sum_over_features equal to False it returns the componentwise
    distances. The :math:`L_1` or block distance is calcualted from summing
    the edge distances [Krause1973]_.

    .. math::

        L_1(X,Y) = \\sum_{i} |X_i-Y_i|

    where :math:`X` and :math:`Y` are the vector set of each sentence :math:`s1,s2`
    respectively.

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

    :Doctest:

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

euclidean_dist_sklearn_doc ="""Computes the paired euclidean distances between X and Y.

    Considering the rows of X (and Y=X) as vectors, compute the
    distance matrix between each pair of vectors.[Deza2009]_

    For efficiency reasons, the euclidean distance between a pair of row
    vector x and y is computed as:

    .. math::

        L_2(X, Y) = \sqrt(\sum_{i} (X_i - Y_i)^2)


    where :math:`X` and :math:`Y` are the vector set of each sentence :math:`s1,s2`
    respectively.

    Optimized equation for computing:

    .. math::

        dist(X, Y) = sqrt(dot(X, X) - 2 * dot(X, Y) + dot(Y, Y))

    :Internal Formula Explanation:

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



    Examples
    --------
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

        L_2(X,Y) = 1-cos(\\frac{{X∩Y}}{\sqrt{X \\cdot Y}})

    where :math:`X` and :math:`Y` are the vector set of each sentence :math:`s1,s2`
    respectively.

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

    :See also:

    sklearn.metrics.pairwise.cosine_similarity
    scipy.spatial.distance.cosine (dense matrices only)
    Read more in the **Sklearn User Guide** :mod:`metrics`.

    """

cocine_similarity_sklearn_doc = ""
