## Howto Document Equations in Python

### scipy.spatial.distance.jaccard(*u*, *v*)

This is the latex style, which is interpreted by Markdown-Typora Processor. 

```latex
\frac{c_{TF} + c_{FT}}{c_{TT} + c_{FT} + c_{TF}}
```

visualize like:

​			$\frac{c_{TF} + c_{FT}}{c_{TT} + c_{FT} + c_{TF}}$

### Pablo en Texsim

Pablo style, it consist on inserting special characters inside texts.

* Disadvantage: E.g. sums symbols doesn't fit to the equation length, must be adapted by hand.    

                               ₂
    euclidean(x,y)= ⎷∑ |x - y |
                      i  i   i

### Pandas

Sphinx style recommendation using the tag *:math:*. 

```reStructuredText
.. math::\alpha = 1 / (1 + com)
```

### scipy.signal.lfilter

*Fancy ASCII* style. 

* Advantage: it can be visualized without any complexity in every text/html processor.
* Disadvantage: E.g. sums symbols doesn't fit to the equation length, must be adapted by hand.    

                             -1               -nb
                 b[0] + b[1]z  + ... + b[nb] z
         Y(z) = ---------------------------------- X(z)
                             -1               -na
                 a[0] + a[1]z  + ... + a[na] z

### sphinx.ext.pngmath				

The *pngmath* sphinx extension generates an embedded PNG with symbols adapted to length equation. See the example below. 

```reStructuredText
.. math::

    y_k = {x_0\over\sqrt{N}} + {1\over\sqrt{N}} \sum_{n=1}^{N-1} x_n \cos\left({\pi n(2k+1) \over 2N}\right) \qquad 0 \le k < N.
```

Visualize as:

​							![Sphinx Matjax Extension example](matjax_png_equation.png)

Same markdown *Tex math* expression google style (using $ character):

​								$y_k = {x_0\over\sqrt{N}} + {1\over\sqrt{N}} \sum_{n=1}^{N-1}x_n \cos\left({\pi n(2k+1) \over 2N}\right)\qquad 0 \le k < N.$

### Analysis

* scipy and numpy propose sphinx *.. math::* expression. scipy, numpy, sklearn and pandas use sphinx to generate very fancy documentation, with very good information recovery feature.
* github can show directly the result of *Tex math* expressions but also PNGs.
* Notebooks can interpret *Tex math* expressions but also PNGs.
* Python consoles as ipython, ipython-qtconsole reflects ugly the *Tex math* expressions. Ipython-Qtconsole can handle PNGs, but not embedded in documentation.

### Conclusions

The best option is to use *Tex math* expressions simplified with *numpy function names* in corresponding cases, and brief explanations about the variables of the equation. See the example below.

$seuclidean_{distance} = np.sum(np.sqrt((A - B)^2 / V))$

*Explanation:* where $A,B$ are the $1D \space vector$ of the sentences, $and$ $V$ is the Inverse Matrix.



**Author: Abel Meneses Abad**

*Date: May 20, 2017*

