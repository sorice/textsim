from .distances import jaccard_ulacia_distance
from .abdi2015 import *
from .filice2015 import *

#This dict strategy is based on sklearn.metrics.pairwaise code example
PAIRED_DISTANCES = {
    'jaccard_ulacia_distance': jaccard_ulacia_distance,
    }


# append all verified distances in module importing argument ALL
__all__ = []
for distance in PAIRED_DISTANCES:
    __all__.append(distance)

__to_implement__ = {
    'Abdi2015': abdi2015_distance
}

__future_implementations__ = {
    'Filice2015': filice2015_graph_distance
}

