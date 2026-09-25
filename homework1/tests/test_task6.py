from src.task6 import open_file, count_words
from pathlib import Path
import pytest

TEST_FILE = Path(__file__).parent.parent / "task6_read_me.txt"

def test_open_file():
    assert isinstance(open_file(TEST_FILE), str)

    assert open_file("this/path/doesnt/exist") == None

@pytest.mark.parametrize("text, expected", [
    ("This is four words.", 4),
    (open_file(TEST_FILE), 104)
])

def test_count_words(text, expected):
    assert count_words(text) == expected