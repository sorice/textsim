from .tokendists import matching_coefficient
from .tokendists import jaccard
from .tokendists import dice_coefficient
from .tokendists import overlap
from .tokendists import euclidean
from .tokendists import manhattan
from .tokendists import binary_distance
from .tokendists import masi_distance
from .tokendists import interval_distance
from .tokendists import jaccard_ulacia

__tokendists__ = [
    'matching_coefficient',
    'jaccard',
    'dice_coefficient',
    'overlap',
    'euclidean',
    'manhattan',
    'binary_distance',
    'masi_distance',
    'interval_distance',
    'jaccard_ulacia',
]

for dist in __tokendists__:
	__all__.append(dist)



importError = False
try:
	import sklearn
except ImportError:
	print('sklearn package most be instaled for some tokendists.')
	pass
finally:
	if not importError:
		from sklearn.metrics.pairwise import manhattan_distances as manhattan_sklearn
		__all__.append('manhattan_sklearn') 
