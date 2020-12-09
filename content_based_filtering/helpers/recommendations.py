from .similarity import get_most_similar_movies
from .movies import get_user_best_ratings

def get_recommendations(movies, ratings, similarity, user_id, top=10):
    """Recommend movies from previously seen movies.
    Args:
        movies (Pandas DataFrame)
        similarity (NumPy Array)
        user_id (int)
        top (int, optional). Default to 10.
    Returns:
        Pandas DataFrame : recommended movies
    """
    best_ratings = get_user_best_ratings(ratings, user_id, top=top)
    movie_ids = best_ratings["movie_id"].drop_duplicates().values

    most_similars = get_most_similar_movies(movies, similarity, movie_ids, top=top)

    return best_ratings.merge(most_similars, left_on="movie_id", right_index=True)
