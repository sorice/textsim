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

:Examples:

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

Where :math:`d_L` is the Levenshtein distance between the string :math:`s1`
and :math:`s2`.

:Citation:

..  [Levenshtein1966] Levenshtein, Vladimir I. (1966).
    Binary Codes Capable of Correcting Deletions, Insertions, and Reversals.
    Soviet Physics Doklady, 10(8):707–710.

:param s1, s2: The strings to be analysed
:type s1: str
:type s2: str
:rtype: float

:Examples:

>>> from nltk.metrics import edit_distance
>>> s1 = 'thisisatest'
>>> s2 = 'testing123testing'
11

"""

jaro_dist_doc = """
The Jaro distance metric takes into account typical spelling deviations.

For two strings X and Y, let :math:`x' = x'_1...x'_{m'}` be the characters in X
that are “common with” Y, and let :math:`y' = y'_1...y'_{n'}` be the charcaters
in Y that are "common with" X. A character a in X is “in common” with Y if the
same character a appears in about the place in Y (in the same order as they
appear in X) [Jaro1989]_.

.. math::

    Jaro(X,Y) = \\frac{1}{3} \\left(\\frac{m'}{n'}+
        \\frac{n'}{n}+\\frac{|1\leq i \leq min(m',n'):x'=y'|}{min(m',n')}\\right)

Where :math:`m,n` are the length in characters of strings :math:`X,Y`
respectively.

:Citation:

.. [Jaro1989] Matthew A. Jaro (1989). "Advances in record linking methodology
    as applied to the 1985 census of Tampa Florida". Journal of the
    American Statistical Society 64:1183-1210. 1989. Publisher Taylor & Francis.

:param s1, s2: The strings to be analysed
:type s1: str
:type s2: str
:rtype: float

:Examples:

>>> from textsim.jellyfish import jaro_distance
>>> s1 = 'dixon'
>>> s2 = 'dicksonx'
0.767...
"""

jaro_winkler_dist_doc = """
This is an extension of the Jaro distance metric, from the work of Winkler in
1990. This extension modifies the weights of poorly matching pairs X,Y that
share a common prefix. The output score is simply adjusted as follows
[Winkler1990]_.

.. math::

    JaroWinkler(X,Y) = Jaro(X,Y)+\\frac{max(4,LCP(X,Y))}{10}*(1-Jaro(X,Y))

where :math:`Jaro(X,Y)` is the Jaro similarity, and :math:`LCP(X,Y)` is the
length of the longest common prefix of X and Y.

:Citation:

.. [Winkler1990] William E. Winkler and Y. Thibaudeau (1990). String Comparator Metrics and Enhanced
    Decision Rules in the Fellegi-Sunter Model of Record Linkage.
    In Proceedings of the Survey Research Methods Section, pages 354–359.

:param s1, s2: The strings to be analysed
:type s1: str
:type s2: str
:rtype: float

:Examples:

>>> from textsim.jellyfish import jaro_distance
>>> s1 = 'dwayne'
>>> s2 = 'duane'
0.84...
"""

hamming_dist_doc = """
This is defined as the number of characters/bits which differ between two
string/binary sequences i.e. the number of bits which need to be
changed (corrupted) to turn one string into the other. For example the bit
strings [Hamming1950]_.

.. math::

    d_H = |{i:1 \leq i \leq n, x_i \neq y_i}|

Where :math:`x_i,y_i` are the characters of strings :math:`X,Y` respectively.

:Citation:

.. [Hamming1950] Richard W. Hamming (1950), "Error detecting and error
    correcting codes". Bell System Technical Journal 29 (2): 147–160, MR 0035935.

:param s1, s2: The strings to be analysed
:type s1: str
:type s2: str
:rtype: float

:Examples:

>>> from textsim.jellyfish import hamming_distance
>>> s1 = 'testing'
>>> s2 = 'this is a test'
13
"""

damerau_levenshtein_dist_doc = """
Is a variation to Levenshtein (Edit) distance. This measure allows the
additional operation of transpositions of adjacent letters (equivalent to one
deletion and one insertion).

.. math::

    no fórmula

:Citation:

.. [Dameau1964] F. Damerau (1964). A technique for computer detection
and correction of spelling errors. Commun. ACM 7, 3 (Mar. 1964), 171–176.

:param s1, s2: The strings to be analysed
:type s1: str
:type s2: str
:rtype: float

:Examples:

>>> from textsim.jellyfish import damerau_levenshtein_distance
>>> s1 = 'cape sand recycling'
>>> s2 = 'edith ann graham'
17
"""

match_rating_comparison_doc = """
Binary comparison.

:param s1, s2: The strings to be analysed
:type s1: str
:type s2: str
:rtype: float

:Examples:

>>> from textsim.jellyfish import match_rating_comparison
>>> s1 = 'Catherine'
>>> s2 = 'Kathryn'
True
"""

needleman_wunch_dist_doc = """
Each of fixed cost q > 0, and character replacements, where the cost of
replacement of i by j is d(i, j). This metric is the minimal total cost of
transforming x into y by these operations. Equivalently, it is:

.. math::

    needleman(X,Y) = min{d_{wH} (x*,y*)},

Where :math:`x*,y*` are strings of length :math:`k,k ≥ max{m, n}`, over the
alphabet :math:`A* = A∪{∗}`, so that, after deleting all new characters ∗,
strings :math:`x*` and :math:`y*` shrink to x and y, respectively.

:Internal Formula Explanation:

... math::

    D(i,j) = min(D(i-1,j-1)+d(s_i,t_j),D(i-1,j)+G,D(i,j-1)+G)

Where :math:`d(i,j)` is a function whereby :math:`d(c,d)=0` if :math:`c=d`, G
in other cases.

:Citation:

.. [Needleman1970] Needleman, S. B. & Wunsch, C. D. A general method applicable
    to the search for similarities in the amino acid sequence of two proteins.
    Journal of Molecular Biology, 1970, 48(3), 443-453.

:param s1, s2: The strings to be analysed
:type s1: str
:type s2: str
:rtype: float

:Examples:

>>> from textsim.jellyfish import needleman_wunch_distance
>>> s1 = 'abcdefg'
>>> s2 = 'bcdfgh'
5
"""
