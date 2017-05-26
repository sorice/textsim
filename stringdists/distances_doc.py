#####!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Complementary documentation for string distances
==================================================

Textsim package additional documentation for distance's doc normalization.

"""

edit_distance_doc = """
Similar to Needleman-Wunch distance but with G=1.

The edit distance is the number of characters that need to be
substituted, inserted, or deleted, to transform s1 into s2.  For
example, transforming "rain" to "shine" requires three steps,
consisting of two substitutions and one insertion:
"rain" -> "sain" -> "shin" -> "shine".  These operations could have
been done in other orders, but at least three steps are needed.

This also optionally allows transposition edits (e.g., "ab" -> "ba"),
though this is disabled by default.

.. math::

    edit\_distance(s1,s2) = min(deletion, insertion, edit)

Operations:

* Copy character from string1 over to string2 (cost 0)
* Delete a character in string1 (cost 1)
* Insert a character in string2 (cost 1)
* Substitute one character for another (cost 1)

The equation of the process can be writed also like this:

.. math::

    d_L(i,j) = min(d_L(i-1,j-1)+d(s_i,t_j),d_L(i-1,j)+1,d_L(i,j-1)+1)

Where :math:`d(i,j)` is a function whereby :math:`d(c,d)=0` if :math:`c=d`, 1
in other cases.

:Citation:

..  [Levenshtein1966] Levenshtein, Vladimir I. (1966).
    Binary Codes Capable of Correcting Deletions, Insertions, and Reversals.
    Soviet Physics Doklady, 10(8):707–710.

:param s1, s2: The strings to be analysed
:param transpositions: Whether to allow transposition edits
:type s1: str
:type s2: str
:type transpositions: bool
:rtype: int

:Doctest:

>>> from nltk.metrics import edit_distance
>>> s1 = 'thisisatest'
>>> s2 = 'testing123testing'
11

"""

edit_similarity_doc = """
The edit similarity is the fraction between the edit distance
and the maximal length between s1 and s2.

.. math::

    edit\_similarity(s1,s2) = 1 - \\frac{d_L(s1,s2)}{max(s1,s2)}

Where :math:`d_L` is the Levenshtein distance between sentences :math:`s1`
and :math:`s2`.

:Citation:

..  [Levenshtein1966] Levenshtein, Vladimir I. (1966).
    Binary Codes Capable of Correcting Deletions, Insertions, and Reversals.
    Soviet Physics Doklady, 10(8):707–710.

:param s1, s2: The strings to be analysed
:type s1: str
:type s2: str
:rtype: float

:Doctest:

>>> from nltk.metrics import edit_distance
>>> s1 = 'thisisatest'
>>> s2 = 'testing123testing'
11

"""
