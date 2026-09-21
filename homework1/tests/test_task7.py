from src.task7 import hash_password
from pytest import raises

def test_hash():
    hash = hash_password("A_password")
    assert hash_password != b"A_password"

def test_small_input():
    with raises(ValueError):
        hash_password("tiny")

def test_int_input():
    with raises(TypeError):
        hash_password(123456789)
