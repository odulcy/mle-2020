def get_movie_id(movies, title, year=None):
    """Retrieve a list of movie id based on a
    title and a year (optional)
    Args:
        movies (Pandas DataFrame)
        title (string)
        year (int, optional). Default to None
    Returns:
       NumPy array : list of int
    """
    res = movies[movies['title'] == title]
    if year:
        res = res[res['year'] == year]
    return res.index.values

def get_movie_name(movies, index):
    """Get a movie by index and return its title
    Args:
        movies (Pandas DataFrame)
        index (int)
    Returns:
        String : title
    """
    return movies.iloc[index]["title"]

def get_movie_year(movies, index):
    """Get a movie by index and return its year
    Args:
        movies (Pandas DataFrame)
        index (int)
    Returns:
        Int : year
    """
    return movies.iloc[index]["year"]

def get_user_best_ratings(ratings, user_id, top=10):
    """Get the best ratings given by user_id on
    the film he has seen.
    Args:
        ratings (Pandas DataFrame)
        user_id (int or list of int)
        top (int, optional). Default to 10
    Returns:
        List of int : movie ids
    """
    rates_from_user = ratings[ratings["user_id"].isin(user_id)]
    rates_from_user = rates_from_user.groupby("user_id").apply(
        lambda x : x.sort_values(by="rating", ascending=False).head(top).reset_index(drop=True)
    )
    rates_from_user = rates_from_user.drop("user_id", axis=1)
    return rates_from_user
