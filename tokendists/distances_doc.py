#####!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Complementary documentation for distances
============================================

Textsim package additional documentation for distance's doc normalization.

"""

from ..decorators import score_original, Appender

try:
    from nltk.metrics import jaccard_distance as jaccard_distance_nltk
except:
    pass

#jaccard_distance_nltk.__doc__ = Appender(jaccard_distance_nltk.__doc__)(jaccard_doc)

jaccard_doc = "%s \nEste es el segundo texto." % jaccard_distance_nltk.__doc__

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
