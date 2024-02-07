"""Test deduplication"""
from dedup import dedup

def test_dedup() -> None:
    result = dedup([1,2,3])
    assert result == [1,2,3]

    result = dedup([1,2,2,3])
    assert result == [1,2,3]

    result = dedup([])
    assert result == []

    restul = dedup(["a","b"])
    assert result == ["a","b"]