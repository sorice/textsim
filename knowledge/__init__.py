from .distances import *

#TODO: filtrar que esté instalado Wornet como se hizo con los otros módulos
from nltk.corpus import wordnet as wn

#This dict strategy is based on sklearn.metrics.pairwaise code example
PAIRED_DISTANCES = {
    'leacock_and_chodorov_distance': leacock_and_chodorov_distance
    }


# append all verified distances in module importing argument ALL
__all__ = []
for distance in PAIRED_DISTANCES:
    __all__.append(distance)

__not_implemented__ = [
    'wu_and_palmer'
]


