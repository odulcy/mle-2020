import pandas as pd


def load_users(path="data/users.csv"):
    """Load user database from a csv file.
    
    Args:
        path (string, path object, or file-like object).
            Defaults to `data/users.csv`
    
    Returns:
        Pandas DataFrame : user database
    """
    users = pd.read_csv(path)
    return users

def load_movies(path="data/movies.csv"):
    """Load user database from a csv file.
    
    Args:
        path (string, path object, or file-like object).
            Defaults to `data/movies.csv`
    
    Returns:
        Pandas DataFrame : user database
    """
    movies = pd.read_csv(path)
    return movies

def load_ratings(path="data/ratings.csv"):
    """Load user database from a csv file.
    
    Args:
        path (string, path object, or file-like object).
            Defaults to `data/ratings.csv`
    
    Returns:
        Pandas DataFrame : user database
    """
    ratings = pd.read_csv(path)
    return ratings
