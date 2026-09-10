from src.task2 import add, same_length, combine_string 

def test_add():
    assert add(1, 2) == 3
    assert add(1.5, 1.5) == 3
    assert add(1, 2.5) == 3.5

def test_same_length():
    assert same_length("Potato", "Tomato") == True
    assert same_length("Success", "Fail") == False

def test_combine_string():
    assert combine_string("What", "ToDO") == "WhatToDO"
    assert combine_string("What", " am I doing") == "What am I doing"