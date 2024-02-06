"""Test navigation."""
import pytest

from navigation import BadMoveError, move


def test_move() -> None:
    """Test moving."""
    position = (0, 0)
    assert move(position, "north") == (0, 1)
    assert move(position, "south") == (0, -1)
    assert move(position, "east") == (1, 0)
    assert move(position, "west") == (-1, 0)


def test_bad_move() -> None:
    """Test bad-move handling."""
    position = (0, 0)
    with pytest.raises(BadMoveError) as excinfo:
        move(position, "down")
    assert "Bad move!" == str(excinfo.value)
