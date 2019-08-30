# Text Similarity Distances

This is a private document to have in just one document the explained reference about similarity equations and  their implementation in text similarity experiments, and the most accurate quotation for exploring deeper.

----------

## String Based

### Binary Distance

0 if strings are equal, 1 if are different.

​:note:​ My self implementation change values: 1 for equal and 0 for different.

### Hamming Distance

The number of characters/bits which need to be changed (corrupted) to turn one string into the other.

$d_H = |{i:1 \leq i \leq n, x_i \neq y_i}|$

### LCS Distance

Ratio of Longest common sub-secuence (LCS) and maximal length between both strings.

$d = \frac{len(LCS)}{max(len(s1),len(s2))}$

$LCS(X,Y) = max(L(i,j)), where\ i,j \in {[0,n];[0,m]}\ and \\ L(i,j) = \begin{cases} 0 & \text{if i=0 or j=0} \\ 1+L(i-1,j-1) & \text{x_i = y_j} \\ max(L(i-1,j),L(i,j-1)) & \text{otherwise} \end{cases}$



$\begin{eqnarray*} \min F(x) \\ \text{subject to } & C_j(X) =  0  ,  &j = 1,...,\text{MEQ}\\& C_j(x) \geq 0  ,  &j = \text{MEQ}+1,...,M\\&  XL  \leq x \leq XU , &I = 1,...,N. \end{eqnarray*}$




### Needleman-Wunch Distance

The minimum edit (*operations*) distance which transforms string1 into string2.

$D(i,j) = min (deletion, insertion, edit) $
​    
    * deletion = D(i,j-1)+G
    * insertion = D(i-1,j)+G
    * edit = D(i-1,j-1) + d(si,tj) //subst/copy
    * d(si,tj) = func for substitution and copy

*Operations*:

* Copy character from string1 over to string2 (cost 0)
* Delete a character in string1 (cost G)
* Insert a character in string2 (cost G)
* Substitute one character for another (cost G)

### Edit & Levenshtein Distance

The minimum edit(*operations*) distance which transforms string1 into string2.
Similar to Needleman-Wunch but with G=1

*Operations*:

* Copy character from string1 over to string2 (cost 0)
* Delete a character in string1 (cost 1)
* Insert a character in string2 (cost 1)
* Substitute one character for another (cost 1)

*Example:*

|       | s    | a    | m    |      | c    | h    | a    | p    | m    | a    | n    |
| ----- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **s** | 0    | 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8    | 9    | 10   |
| **a** | 1    | 0    | 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8    | 9    |
| **m** | 2    | 1    | 0    | 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8    |
|       | 3    | 2    | 1    | 0    | 1    | 2    | 3    | 4    | 5    | 6    | 7    |
| **j** | 4    | 3    | 2    | 1    | 1    | 2    | 3    | 4    | 5    | 6    | 7    |
| **o** | 5    | 4    | 3    | 2    | 2    | 2    | 3    | 4    | 5    | 6    | 7    |
| **h** | 6    | 5    | 4    | 3    | 3    | 2    | 3    | 4    | 5    | 6    | 7    |
| **n** | 7    | 6    | 5    | 4    | 4    | 3    | 3    | 4    | 5    | 6    | 6    |
|       | 8    | 7    | 6    | 5    | 5    | 4    | 4    | 4    | 5    | 6    | 7    |
| **c** | 9    | 8    | 7    | 6    | 5    | 5    | 5    | 5    | 5    | 6    | 7    |
| **h** | 10   | 9    | 8    | 7    | 6    | 5    | 6    | 6    | 6    | 6    | 7    |
| **a** | 11   | 10   | 9    | 8    | 7    | 6    | 5    | 6    | 7    | 6    | 7    |
| **p** | 12   | 11   | 10   | 9    | 8    | 7    | 6    | 5    | 6    | 7    | 7    |
| **m** | 13   | 12   | 11   | 10   | 9    | 8    | 7    | 6    | 5    | 6    | 7    |
| **a** | 14   | 13   | 12   | 11   | 10   | 9    | 8    | 7    | 6    | 5    | 6    |
| **n** | 15   | 14   | 13   | 12   | 11   | 10   | 9    | 8    | 7    | 6    | 5    |

### Damerau - Levenshtein Distance

Same as Levenshtein but only replacement, indels and transposition.

### Jaro Distance Distance

$Jaro(X,Y) = \frac{1}{3} \left(\frac{m'}{n'}+\frac{n'}{n}+\frac{|1\leq i \leq min(m',n'):x'=y'|}{min(m',n')}\right)$

### Jaro Winkler Distance

$JaroWinkler(X,Y) = Jaro(X,Y)+\frac{max(4,LCP(X,Y))}{10}*(1-Jaro(X,Y))$

where `Jaro(X,Y)` is the Jaro similarity, and `LCP(X,Y)` is the
length of the longest common prefix of X and Y.

### Smith-Waterman Distance

### Dice Coefficient Distance

### Gotoh & Smith-Waterman-Gotoh Distance

### Monge-Elkan Distance Distance

.

-------------------------

## Token Based

### Jaccard

$jaccard(X,Y) = \frac {|X ∩ Y|}{|X ∪ Y|}$

### Masi Distance

$masi(X,Y) = 1 - \frac {|X ∩ Y|}{|X ∪ Y|*m}$

* :math:`m = 1` if :math:`|X ∩ Y| = |X| = |Y|`
* :math:`m = 0.67` if :math:`|X ∩ Y| = min(|X|,|Y|)`
* :math:`m = 0.33` if :math:`|X ∩ Y| > 0`
* :math:`m = 0` if :math:`|X ∩ Y| = 0`

### Interval Distance

$interval(X,Y) = (|X - |X ∩ Y||)^2$

### Manhattan & Block & L1 & City

$L_1(X,Y) = \sum_{i} |X_i-Y_i|$

### Euclidean Distance

$L_2(X, Y) = \sqrt(\sum_{i} (X_i - Y_i)^2)$

### Cosine Distance

$cos(X,Y) = 1 - \cos\left({|X ∩ Y|\over\sqrt{|X|·|Y|}}\right)$

$cos(X,Y) = \frac{\sum_{i}X_i*Y_i}{\sqrt{\sum_iX_i^2*\sum_iY_i^2}}$

.

--------------------

## Corpus Based

.

---------------

## Knowledge Based

.

-----------------------

## Graph Based

.

Author: Abel Meneses-Abad

Year: 2017