import pytest
import numpy as np
from content_based_filtering.helpers.similarity import get_most_similar_by_id

similarity = np.array([
    [3, 1, 1],
    [1, 3, 0],
    [1, 0, 2]
])

test_args = [
    (similarity, [0], 1, np.array([[2]])),
    (similarity, [0], 2, np.array([[2, 1]])),
    (similarity, [1], 2, np.array([[0, 2]])),
    (similarity, [2], 2, np.array([[0, 1]])),
    (similarity, [0], 100, np.array([[2, 1]])),
    (similarity, [0,1], 2, np.array([[2, 1],[0, 2]]))
]

@pytest.mark.parametrize("similarity, movie_id, top, expected", test_args)
def test_get_most_similar_by_id(similarity, movie_id, top, expected):
    assert np.all(get_most_similar_by_id(similarity, movie_id, top) == expected)
