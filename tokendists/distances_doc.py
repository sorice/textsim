#####!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Complementary documentation for distances
============================================

Textsim package additional documentation for distance's doc normalization.

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
:returns: float

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
:returns: float

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
