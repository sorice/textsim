from .stringdists import lcs
from .stringdists import longlcs
from .stringdists import damerau_levenshtein_distance

__all__ = [
	'lcs',
	'longlcs',
	'damerau_levenshtein_distance',

] 

importError = False
try:
	import nltk
except ImportError:
	print('NLTK package most be instaled for some stringdists.')
	pass
finally:
	if not importError:
		from nltk.metrics import edit_distance
		__all__.append('edit_distance')