from .tokendists import jaccard_distance_textsim
from .tokendists import dice_coefficient_textsim
from .tokendists import overlap_distance_textsim
from .tokendists import euclidean_distance_textsim
from .tokendists import matching_coefficient_textsim
from .tokendists import matching_coefficient_pablo
from .tokendists import containment_similarity_textsim

#This dict strategy is based on sklearn.metrics.pairwaise code example
PAIRED_DISTANCES = {
    'jaccard_distance_textsim': jaccard_distance_textsim,
    'dice_coefficient_textsim': dice_coefficient_textsim,
    'overlap_distance_textsim': overlap_distance_textsim,
    'euclidean_distance_textsim': euclidean_distance_textsim,
    'matching_coefficient_textsim': matching_coefficient_textsim,
    'matching_coefficient_pablo': matching_coefficient_pablo,
    'containment_similarity_textsim': containment_similarity_textsim,
    }

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
        from .tokendists import (jaccard_distance_nltk, masi_distance, interval_distance)

        PAIRED_DISTANCES['jaccard_distance_nltk'] = jaccard_distance_nltk
        PAIRED_DISTANCES['masi_distance'] = masi_distance
        PAIRED_DISTANCES['interval_distance'] = interval_distance


SklearnImportError = False
try:
    import sklearn
except ImportError:
    print("Some tokendists will not be available due to Sklearn package isn't installed.")
    pass
finally:
    if not SklearnImportError:
        from .tokendists import manhattan_distance_sklearn
        from .tokendists import cosine_distance_sklearn
        from .tokendists import cosine_similarity_sklearn
        from .tokendists import euclidean_distance_sklearn

        PAIRED_DISTANCES['manhattan_distance_sklearn'] = manhattan_distance_sklearn
        PAIRED_DISTANCES['cosine_distance_sklearn'] = cosine_distance_sklearn
        PAIRED_DISTANCES['cosine_similarity_sklearn'] = cosine_similarity_sklearn
        PAIRED_DISTANCES['euclidean_distance_sklearn'] = euclidean_distance_sklearn

ScipyImportError = False
try:
    import scipy
except ImportError:
    print("Some tokendists will not be available due to Scipy package isn't installed.")
    pass
finally:
    if not ScipyImportError:
        from .tokendists import (jaccard_distance_scipy,
                            braycurtis_distance_scipy, canberra_distance_scipy,
                            chebyshev_distance_scipy, cityblock_distance_scipy,
                            correlation_distance_scipy, cosine_distance_scipy,
                            dice_distance_scipy, euclidean_distance_scipy,
                            hamming_distance_scipy, kulsinski_distance_scipy,
                            mahalanobis_distance_scipy, matching_distance_scipy,
                            minkowski_distance_scipy,
                            rogerstanimoto_distance_scipy,
                            russellrao_distance_scipy,
                            seuclidean_distance_scipy,
                            sokalmichener_distance_scipy,
                            sokalsneath_distance_scipy,
                            sqeuclidean_distance_scipy,
                            yule_distance_scipy
                            )

        PAIRED_DISTANCES['braycurtis_distance_scipy'] = braycurtis_distance_scipy
        PAIRED_DISTANCES['canberra_distance_scipy'] = canberra_distance_scipy
        PAIRED_DISTANCES['chebyshev_distance_scipy'] = chebyshev_distance_scipy
        PAIRED_DISTANCES['cityblock_distance_scipy'] = cityblock_distance_scipy
        PAIRED_DISTANCES['correlation_distance_scipy'] = correlation_distance_scipy
        PAIRED_DISTANCES['cosine_distance_scipy'] = cosine_distance_scipy
        PAIRED_DISTANCES['dice_distance_scipy'] = dice_distance_scipy
        PAIRED_DISTANCES['euclidean_distance_scipy'] = euclidean_distance_scipy
        PAIRED_DISTANCES['hamming_distance_scipy'] = hamming_distance_scipy
        PAIRED_DISTANCES['jaccard_distance_scipy'] = jaccard_distance_scipy
        PAIRED_DISTANCES['kulsinski_distance_scipy'] = kulsinski_distance_scipy
        PAIRED_DISTANCES['mahalanobis_distance_scipy'] = mahalanobis_distance_scipy
        PAIRED_DISTANCES['matching_distance_scipy'] = matching_distance_scipy
        PAIRED_DISTANCES['minkowski_distance_scipy'] = minkowski_distance_scipy
        PAIRED_DISTANCES['rogerstanimoto_distance_scipy'] = rogerstanimoto_distance_scipy
        PAIRED_DISTANCES['russellrao_distance_scipy'] = russellrao_distance_scipy
        PAIRED_DISTANCES['seuclidean_distance_scipy'] = seuclidean_distance_scipy
        PAIRED_DISTANCES['sokalmichener_distance_scipy'] = sokalmichener_distance_scipy
        PAIRED_DISTANCES['sokalsneath_distance_scipy'] = sokalsneath_distance_scipy
        PAIRED_DISTANCES['sqeuclidean_distance_scipy'] = sqeuclidean_distance_scipy
        PAIRED_DISTANCES['yule_distance_scipy'] = yule_distance_scipy

#After performance we compute result and stablished default edit, levenshtein
#damerau-levenshtein
# from .tokendists import jaccard_distance_XXX as jaccard_distance

# PAIRED_DISTANCES['jaccard_distance'] = jaccard_distance



# append all verified distances in module importing argument ALL
__all__ = []
for distance in PAIRED_DISTANCES:
    __all__.append(distance)

__not_implemented__ = [
    'Kullback-Leibler distance',  #test later from scipy.special import kl_div
    'Hellinger distance',
    'Jensen Shanon divergence',
    'Harmonic Mean distance',     #se puede implementar usando numpy
    'Skew divergence',
    'Tau distance',
    'Q-gram distance',            #se puede implementar fácil
    'Q-gram Overlap',
    'Skip-grams distance',
    'Greedy String Tiling'
]
