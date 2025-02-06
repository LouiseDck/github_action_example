import pytest
from src.algorithm import very_complex_algorithm

def test_algorithm():
    result = very_complex_algorithm(5, 5)
    assert result.shape == (3, 7)

def test_wrong_params():
    with pytest.raises(ValueError):
        very_complex_algorithm(0, 0)
