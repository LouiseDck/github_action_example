import pytest
from src.algorithm import very_complex_algorithm

def test_algorithm():
    result = very_complex_algorithm(5, 5)
    assert result.shape == (3, 7)

def test_result():
    # test that all elements are between 1 and 100
    result = very_complex_algorithm(5, 5)
    assert (result >= 1).all()
    assert (result <= 100).all()

def test_wrong_params():
    with pytest.raises(ValueError):
        very_complex_algorithm(0, 0)
