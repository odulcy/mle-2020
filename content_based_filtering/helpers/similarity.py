import numpy as np
import pandas as pd

from .movies import get_movie_id, get_movie_name

def pairsimilarity(feature_matrix):
    """Compute pairwise similarity between objects.
    If $x_1$ and $x_2$ are objects, 
    Similarity is defined as follow :

    $similarity(x_1, x_2) = \sum_{i=1}^n x_{1i} x_{2i}$
        where $x_{1i}$ and $x_{2i}$ are 0-1 values.

    Args:
        feature_matrix (NumPy array or Pandas DataFrame)

    Returns:
        NumPy array or Pandas DataFrame : pairwise similarity
    """
    return feature_matrix.dot(feature_matrix.T)


def get_most_similar_by_id(similarity, index, top=10):
    """Get most similar items to a given item.
    Args:
        similarity (NumPy array)
        index (array like)
        top (int, optional). Default to 10
    Returns:
        Movie id
    """
    assert top >= 0, "top needs to be a non-negative value"
    top = min(top,len(similarity))

    # Sort by best similarity
    best = similarity[index].argsort()[:,::-1]
    best_without_duplicate = []

    # A movie is obviously similar to itself
    # Delete its id, if present
    # To keep a top 10 for instance
    for i in range(best.shape[0]):
        mask = (best[i] != index[i])
        best_without_duplicate.append(best[i,mask])

    return np.array(best_without_duplicate)[:,:top]

def get_most_similar_movies(movies, similarity, requested_movies, top=10):
    """Get most similar movies to a given movie by names.
    Args:
        movies (Pandas DataFrame)
        similarity (NumPy array)
        requested_movies (list of names or id) : if strings are provided, the function will
            perform a look up to find corresponding id. Otherwise, integers must be provided.
        year (int, optional). Default to None.
        top (int, optional). Default to 10
    Returns:
        Movie id
    """
    assert top >= 0, "top needs to be a non-negative value"
    
    all_int = all(isinstance(x, (int, np.integer)) for x in requested_movies)
    all_str = all(isinstance(x, str) for x in requested_movies)
    
    assert (all_int and not all_str) or (not all_int and all_str), "movie should be all name or all id"
    
    top = min(top,similarity.shape[0])
    
    index = []

    if all_str:
        index = np.concatenate([
            get_movie_id(movies, name)
            for name in requested_movies
        ])
    else:
        index = requested_movies

    most_similar_movies = get_most_similar_by_id(similarity, index, top=top)

    film_ranks = np.arange(1,top+1)
    recommended_movies = pd.DataFrame(index=index, data=most_similar_movies, columns=film_ranks)
    recommended_movies = recommended_movies.applymap(
        lambda x : (x, get_movie_name(movies, x)) 
    )

    return pd.concat([movies.iloc[index][["title", "year"]], recommended_movies], axis=1)
