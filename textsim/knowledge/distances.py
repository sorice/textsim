#####!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Knowledge Based Similarity Distances
==================================

Similarity measures based on knowledge data bases.
This version contains Wordnet resource database to calculate distances.

Main implementations comes from NLTK package.
This is a more reduced area of develop, only few implementations are available
on international papers citations.

"""

__author__ = 'Abel Meneses-Abad'

import nltk
from nltk.corpus import wordnet as wn

def leacock_and_chodorov_distance(s1,s2):
    return wn.lch_similarity
