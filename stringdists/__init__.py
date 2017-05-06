from .stringdists import lcs
from .stringdists import longlcs
from .stringdists import damerau_levenshtein_distance
# from .stringdists import edit_distance

__distances__ = [
	'lcs',
	'longlcs',
	'damerau_levenshtein_distance',
]

# __jellyfish__ = [
# 	'levenshtein_distance',
# ]

# for distance in __jellyfish__ and not JellyfishImportError:
# 	__all__.append(distance)

#Import nltk distances from ~/nltk/metric/distance.py and modify after with decorators
global NLTKImportError
NLTKImportError = False
try:
    import nltk
except ImportError:
    NLTKImportError = True
    print("Some stringdists will not be available due to NLTK package isn't installed.")
    pass
finally:
    if not NLTKImportError:
        from .stringdists import edit_distance

        __nltk_distances__ = [
        	'edit_distance',
        ]

        for distance in __nltk_distances__:
            __distances__.append(distance)

# append all verified distances in module importing argument ALL
__all__ = []
for distance in __distances__:
	__all__.append(distance)
