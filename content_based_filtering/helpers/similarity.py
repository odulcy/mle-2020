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
