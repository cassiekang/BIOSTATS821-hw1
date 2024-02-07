import pytest

from multiplication import times

def test_times_with_even_values() -> None:
    """Test multiplication.times()."""
    result = times(2,3) #act
    assert result == 6

    for a in range(5):
        for b in range(5):
            assert times(a,b) == a*b


def test_avg()->None:
    """Test avg()"""
    result = avg([3,4])
    assert result == 3,5

    result = avg([3,103])
    assert result == 53