from .stringdists import (lcs, lcs_distance,
                            damerau_levenshtein_distance_textsim,
                            smith_waterman_distance)

__distances__ = [
	'lcs',
	'lcs_distance',
	'damerau_levenshtein_distance_textsim',
    'smith_waterman_distance',
]

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
        from .stringdists import (edit_distance_nltk, binary_distance)

        __nltk_distances__ = [
        	'edit_distance_nltk',
            'binary_distance',
        ]

        for distance in __nltk_distances__:
            __distances__.append(distance)

JellyfishImportError = False
try:
    from .jellyfish import levenshtein_distance #change later for import jellyfish
except:
    JellyfishImportError = True
    print("Some stringdists will not be available due to Jellyfish package isn't installed.")
    pass
finally:
    if not JellyfishImportError:
        from .stringdists import levenshtein_distance as levenshtein_distance_jellyfish
        from .stringdists import levenshtein_distance as levenshtein_distance
        from .stringdists import levenshtein_distance as edit_distance
        from .jellyfish import jaro_distance, hamming_distance
        from .jellyfish import jaro_winkler as jaro_winkler_distance

        __jellyfish_distances__ = [
            'levenshtein_distance_jellyfish',
            'levenshtein_distance',
            'edit_distance',
            'jaro_distance',
            'jaro_winkler_distance',
            'hamming_distance',
        ]

        for distance in __jellyfish_distances__:
            __distances__.append(distance)

from .pattern import levenshtein as levenshtein
from .pattern import levenshtein_similarity as levenshtein_distance_pattern
from .pattern import levenshtein_similarity as damerau_levenshtein_distance
from .pattern import dice_coefficient as dice_coefficient_pattern

__pattern_distances__ = [
    'levenshtein',
    'levenshtein_distance_pattern',
    'damerau_levenshtein_distance',
    'dice_coefficient_pattern',
]

for distance in __pattern_distances__:
    __distances__.append(distance)

# append all verified distances in module importing argument ALL
__all__ = []
for distance in __distances__:
	__all__.append(distance)

__not_implemented__ = [
    'Neeldman-Wunch distance',
    'Gotoh distance',
    'Monge Elkan distance',
]
