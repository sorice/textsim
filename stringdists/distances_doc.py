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
:type s1, s2: str
:type transpositions: bool
:rtype: int

:Examples:

>>> from nltk.metrics import edit_distance
>>> s1 = 'thisisatest'
>>> s2 = 'testing123testing'
>>> edit_distance(s1,s2)
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
:type s1, s2: str
:rtype: float

:Examples:

>>> from textsim.stringdists import edit_similarity_nltk
>>> s1 = 'thisisatest'
>>> s2 = 'testing123testing'
>>> edit_similarity_nltk(s1,s2)
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
:type s1, s2: str
:rtype: float

:Examples:

>>> from textsim.jellyfish import jaro_distance
>>> s1 = 'dixon'
>>> s2 = 'dicksonx'
>>> jaro_distance(s1,s2)
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
:type s1, s2: str
:rtype: float

:Examples:

>>> from textsim.jellyfish import jaro_distance
>>> s1 = 'dwayne'
>>> s2 = 'duane'
>>> jaro_distance(s1,s2)
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
:type s1, s2: str
:rtype: float

:Examples:

>>> from textsim.jellyfish import hamming_distance
>>> s1 = 'testing'
>>> s2 = 'this is a test'
>>> hamming_distance(s1,s2)
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
:type s1, s2: str
:rtype: float

:Examples:

>>> from textsim.jellyfish import damerau_levenshtein_distance
>>> s1 = 'cape sand recycling'
>>> s2 = 'edith ann graham'
>>> damerau_levenshtein_distance(s1,s2)
17
"""

match_rating_comparison_doc = """
Binary comparison.

:param s1, s2: The strings to be analysed
:type s1, s2: str
:rtype: float

:Examples:

>>> from textsim.jellyfish import match_rating_comparison
>>> s1 = 'Catherine'
>>> s2 = 'Kathryn'
>>> match_rating_comparison(s1,s2)
True
"""

needleman_wunsch_dist_doc = """
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

Operations:

    * :math:`D(i-1,j-1) + d(x_i,y_j)` if SUBST/COPY
    * :math:`D(i-1,j) + G` if INSERT
    * :math:`D(i,j-1) + G` if DELETE

:Citation:

.. [Needleman1970] Needleman, S. B. & Wunsch, C. D. A general method applicable
    to the search for similarities in the amino acid sequence of two proteins.
    Journal of Molecular Biology, 1970, 48(3): 443-453.

:param s1, s2: The strings to be analysed
:type s1, s2: str
:param G: gap cost value, default value 2
:rtype: float

:Examples:

>>> from textsim.jellyfish import needleman_wunsch_distance
>>> s1 = 'abcdefg'
>>> s2 = 'bcdfgh'
>>> needleman_wunsch_distance(s1,s2)
5
"""

lcs_doc = """
For two strings X and Y, let :math:`x = x_1...x_m` be the characters in X
and :math:`y = y_1...y_n` be the charcaters in Y. Over some alphabet, lcs
find the longest string S that is a subsequence of both X and Y [allison1986]_.

.. math::

    LCS(X,Y) = max(L(i,j)), where\ i,j \in {[1,n];[1,m]}

Where :math:`m,n` are the length in characters of strings :math:`X,Y`
respectively and

.. math::

    L(i,j) = \\begin{cases} 0          & {if\ i=0\ or\ j=0}
            \\\ 1+L(i-1,j-1)           & {x_i = y_j}
            \\\ max(L(i-1,j),L(i,j-1)) & otherwise \end{cases}

:Citation:

.. [allison1986] Lloyd Allison & Trevor I. Dix (1986).
    A bit-string longest-common-subsequence algorithm.
    Information Processing Letters, Elsevier, 1986, 23(5): 305-310.

:param s1, s2: The strings to be analysed
:type s1, s2: str
:rtype: str

:Examples:

>>> from textsim.strindists import lcs
>>> s1 = 'thisisatest'
>>> s2 = 'testing123testing'
>>> lcs(s1, s2) == 'tsitest'
True

"""

lcs_similarity_doc = """
Given the longest common substring (LCS) between X and Y, the lcs_similarity
is the harmonic mean of the LCS/len(X) and LCS/len(Y).

:param s1, s2: The strings to be analysed
:type s1, s2: str
:rtype: float

:Examples:

>>> from textsim.strindists import lcs, lcs_similarity
>>> s1 = "jellyfish"
>>> s2 = "smellyfishs"
>>> lcs_similarity(s1,s2) == 0.7272727272727273
True

:See also:

:func:`textsim.strindists.lcs` for LCS understanding.
"""

smith_waterman_dist_doc = """
Similar to Edit distance ranking operations to optimal aligned both compared
strings, in this case convert s2 in s1. This distance indicates de longest
substring that match in both strings.

This function have two additional parameters: match
and mismatch to weight the values if chars match or not. The algorithm
stablished a gap cost for char insertion and deletion.

.. math:

    D(i,j) = max(d(i-1,j-1)-d(x_i,y_j),d_L(i-1,j)+1,d_L(i,j-1)+1)

where :math:`D(i,j)` is maximum value over all i,j in table. :math:`X,Y` are
the initial sentences and :math:`x = x_1...x_m` and :math:`y = y_1...y_n` are
the characters in X and Y respectively.

Operations:

    * 0 if start over
    * :math:`D(i-1,j-1)-d(x_i,y_j)` if SUBST/COPY
    * :math:`D(i-1,j)-G` if INSERT
    * :math:`D(i,j-1)-G` if DELETE

Where :math:`d(i,j)` is a function whereby :math:`d(i,j)=match` if x_i = y_j,
else :math:`d(i,j)=mismatch` if :math:`x_i \neq y_j`. :math:`G` is the gap cost
value.

:Citation:

.. [smith1981] Temple F. Smith & Michel S. Waterman (1981).
    Identification of common molecular subsequences.
    Journal of molecular biology 147(1): 195-197. Elsevier.

:param s1, s2: The strings to be analysed
:type s1, s2: str
:param match, mismatch: context dependent substitution cost
:type match, mismatch: int, default values 2,-1
:param G: gap cost value, default value 1
:rtype: float

:Examples:

>>> from textsim.stringdists import smith_waterman_distance
>>> s1 = "aaaa mnop zzzz"
>>> s2 = "bbbb mnop yyyy"
>>> smith_waterman_distance (s1,s2, match=2,mismatch=-1,gap_cost=1)
12.0

"""

dice_doc = """
Returns the similarity between string1 and string1 as a number between [0,1]
based on the number of shared character bigrams. E.g., "night" and "nacht"
have one common bigram "ht" [dice1945]_.

.. math:

    dice(X,Y) = \\frac{2*|ngrams(X) ∩ ngrams(Y)|}{|ngrams(X)|+|ngrams(Y)|}


Where :math:`X` and :math:`Y` are the initial strings to be compare, and
:math:`ngrams(z)` returns the set of n-grams of the string z. This function is
implemented internaly.

:Citation:

.. [dice1945] Lee R. Dice (1945).
    Measures of the amount of ecologic association between species.
    Journal of Ecology 26(3): 297-302. Wiley Online Library

:param s1, s2: The strings to be analysed
:type s1, s2: str
:rtype: float

:Examples:
>>> from textsim.strindists import dice_coefficient_pattern
>>> s1 = "jellyfish"
>>> s2 = "smellyfishs"
>>>dice_coefficient_pattern(s1,s2)
0.777...
"""

containment_similarity_doc = """
Similar to the Dice coefficient, the containment measure calculates the
intersection of n-grams between both strings but normalises them only with
respect to the elements in the suspicious string. Commonly used in text reuse
field to calculate similarity between documents.

.. math::

    containment(X,Y) = \\frac{|ngrams(X) ∩ ngrams(Y)|}{|ngrams(X)|}

Where :math:`X` and :math:`Y` are the initial strings to be compare, and
:math:`ngrams(z)` returns the set of n-grams of the string z. This function is
implemented internaly.

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



