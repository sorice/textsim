from .tokendists import matching_coefficient
from .tokendists import jaccard_distance_textsim
from .tokendists import dice_coefficient_textsim
from .tokendists import overlap_distance_textsim
from .tokendists import euclidean_distance_textsim
# from .tokendists import jaccard_ulacia

__distances__ = [
    'matching_coefficient',
    'jaccard_distance_textsim',
    'dice_coefficient_textsim',
    'overlap_distance_textsim',
    'euclidean_distance_textsim',
    # 'jaccard_ulacia',
]

#Import nltk token distances from ~/nltk/metric/distance.py and modify after with decorators
NLTKImportError = False
try:
    import nltk
except ImportError:
    NLTKImportError = True
    print("Some tokendists will not be available due to NLTK package isn't installed.")
    pass
finally:
    if not NLTKImportError:
        from .tokendists import (jaccard_distance, masi_distance, interval_distance)

        __nltk_distances__ = [
            'jaccard_distance',
             'masi_distance',
             'interval_distance',
        ]

        for distance in __nltk_distances__:
            __distances__.append(distance)

SklearnImportError = False
try:
    import sklearn
except ImportError:
    print("Some tokendists will not be available due to Sklearn package isn't installed.")
    pass
finally:
    if not SklearnImportError:
        from .tokendists import manhattan_distance as manhattan_distance_sklearn
        from .tokendists import cosine_distance as cosine_distance_sklearn
        from .tokendists import euclidean_distance as euclidean_distance_sklearn
        __distances__.append('manhattan_distance_sklearn')
        __distances__.append('cosine_distance_sklearn')
        __distances__.append('euclidean_distances_sklearn')

ScipyImportError = False
try:
    import scipy
except ImportError:
    print("Some tokendists will not be available due to Scipy package isn't installed.")
    pass
finally:
    if not ScipyImportError:
        from .tokendists import jaccard_distance_scipy
        __distances__.append('jaccard_distance_scipy')

# append all verified distances in module importing argument ALL
__all__ = []
for distance in __distances__:
    __all__.append(distance)

__not_implemented__ = [
    # 'Gotoh distance',
    # 'Monge Elkan distance',
]
