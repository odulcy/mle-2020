def get_movie_id(movies, title, year=None):
    """Retrieve a list of movie id based on a
    title and a year (optional)
    Args:
        movies (Pandas DataFrame)
        title (string)
        year (int, optional). Default to None
    Returns:
        Pandas Index
    """
    res = movies[movies['title'] == title]
    if year:
        res = res[res['year'] == year]
    return res.index

def get_movie_name(movies, index):
    """Get a movie by index and return its title
    Args:
        movies (Pandas DataFrame)
        index (int)
    Returns:
        String : title
    """
    return movies.iloc[index].title

def get_movie_year(movies, index):
    """Get a movie by index and return its year
    Args:
        movies (Pandas DataFrame)
        index (int)
    Returns:
        Int : year
    """
    return movies.iloc[index].year
