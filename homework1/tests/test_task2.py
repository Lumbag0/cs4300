from src.task2 import add, same_length, combine_string 
import pytest

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (1.5, 1.5, 3),
    (1, 2.5, 3.5)
])

def test_add(a, b, expected):
    assert add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    ("Potato", "Tomato", True),
    ("Success", "Fail", False)
])

def test_same_length(a, b, expected):
    assert same_length(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    ("What", "ToDO", "WhatToDO"),
    ("What", " am I doing", "What am I doing")
])

def test_combine_string(a, b, expected):
    assert combine_string(a, b) == expected