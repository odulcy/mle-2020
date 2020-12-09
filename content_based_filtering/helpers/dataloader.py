import pandas as pd

def load_users(path):
    """Load users database from a csv file.
    
    Args:
        path (string, path object, or file-like object).
            Defaults to `data/users.csv`
    
    Returns:
        Pandas DataFrame : users database
    """
    users = pd.read_csv(path)
    users.set_index("user_id", inplace=True)
    users.sort_index(inplace=True)
    return users

def load_movies(path):
    """Load movies database from a csv file.
    
    Args:
        path (string, path object, or file-like object).
            Defaults to `data/movies.csv`
    
    Returns:
        Pandas DataFrame : movies database
    """
    movies = pd.read_csv(path)
    movies.loc[:, movies.dtypes == 'float64'] = movies.loc[:, movies.dtypes == 'float64'].astype('int8')
    movies.set_index("movie_id", inplace=True)
    movies.sort_index(inplace=True)
    return movies

def load_ratings(path):
    """Load ratings database from a csv file.
    
    Args:
        path (string, path object, or file-like object).
            Defaults to `data/ratings.csv`
    
    Returns:
        Pandas DataFrame : ratings database
    """
    ratings = pd.read_csv(path)
    return ratings
