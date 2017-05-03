"""
Text Similarity Measures for Python
==================================

textsim is a Python module integrating classical distances for text
similarity evaluation. The library reuse well known implementations
of Gensim, NLTK and other classical python libraries for text 
processing.

It aims to provide simple solutions to text similarity problems.
Paraphrase detection, text reuse and many other NLP problems needs
deep feature extraction for good results. This compendium of text
distances intend to improve the machine learning process for
this kind of problems.

See https://github.com/sorice/textsim for complete documentation.
"""

__version__ = '0.1'

# Copyright notice
__copyright__ = """\
Copyright (C) 2017-2020 QtNLP Project.

Distributed and Licensed under the BSD License, Version X.X and 
LTPL License, Version 1.0, which are included by reference.
"""
__license__ = "BSD License, Version X.X and LTPL License, Version 1.0"

__keywords__ = ['computational linguistics', 'corpus based distance',
                'knowledge based distance', 'text similarity',
                'text representation models', 'linguistics', 'text',
                'distance', 'text analytics']

__url__ = "https://github.com/sorice/textsim"

__maintainer__ = "Abel Meneses-Abad, Leonel Salazar-Videaux"
__maintainer_email__ = "abelma1980@gmail.com"
__author__ = __maintainer__
__author_email__ = __maintainer_email__

# "Trove" classifiers for Python Package Index.
__classifiers__ = [
    'Development Status :: 1 - Production',
    'Intended Audience :: Developers',
    'Intended Audience :: Education',
    'Intended Audience :: Information Technology',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3.5',
    'Topic :: Scientific/Engineering',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'Topic :: Scientific/Engineering :: Human Machine Interfaces',
    'Topic :: Scientific/Engineering :: Information Analysis',
    'Topic :: Scientific/Engineering :: Text Data Mining',
    'Topic :: Text Processing',
    'Topic :: Text Processing :: Filters',
    'Topic :: Text Processing :: General',
    'Topic :: Text Processing :: Indexing',
    'Topic :: Text Processing :: Linguistic',
]

from .stringdists import lcs
from .stringdists import longlcs
from .stringdists import damerau_levenshtein_distance

from .tokendists import matching_coefficient
from .tokendists import jaccard
from .tokendists import dice_coefficient
from .tokendists import overlap
from .tokendists import euclidean
from .tokendists import manhattan
from .tokendists import edit_distance
from .tokendists import binary_distance
from .tokendists import masi_distance
from .tokendists import interval_distance
from .tokendists import jaccard_ulacia

__all__ = [
    'lcs',
    'longlcs',
    'damerau_levenshtein_distance',
    'matching_coefficient',
    'jaccard',
    'dice_coefficient',
    'overlap',
    'euclidean',
    'manhattan',
    'edit_distance',
    'binary_distance',
    'masi_distance',
    'interval_distance',
    'jaccard_ulacia',
]