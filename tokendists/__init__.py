from .tokendists import matching_coefficient
# from .tokendists import jaccard
# from .tokendists import dice_coefficient
# from .tokendists import overlap
# from .tokendists import euclidean
# from .tokendists import manhattan
# from .tokendists import binary_distance
# from .tokendists import masi_distance
# from .tokendists import interval_distance
# from .tokendists import jaccard_ulacia

__distances__ = [
    'matching_coefficient',
    # 'jaccard',
    # 'dice_coefficient',
    # 'overlap',
    # 'euclidean',
    # 'manhattan',
    # 'binary_distance',
    # 'masi_distance',
    # 'interval_distance',
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
        from .tokendists import (jaccard_distance)

        __nltk_distances__ = [
            'jaccard_distance',
            # 'binary_distance',
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
		__distances__.append('manhattan_distance_sklearn')

# append all verified distances in module importing argument ALL
__all__ = []
for distance in __distances__:
    __all__.append(distance)

__not_implemented__ = [
    # 'Gotoh distance',
    # 'Monge Elkan distance',
]
