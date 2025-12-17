from src.service import BERRIES, calculate_some_value
import pytest


pytest_plugins = ("pytest_asyncio",)


def test_berries_suffix():
    """All berries mush have 'berry' suffix"""
    assert all(berry.endswith("berry") for berry in BERRIES)


def test_berries_no_tomato():
    """There must never be a tomato"""
    assert all(berry != "tomato" for berry in BERRIES)


@pytest.mark.asyncio
@pytest.mark.parametrize("x, expected", [
    (0, 123),
    (-123, 0),
    (1, 124),
    (101, 224),
    (6713263138, 6713263261),
    (-2230123, -2230000)
])
async def test_calculate_some_value(x: int, expected: int):
    assert (await calculate_some_value(x)) == expected
