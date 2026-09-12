from src.task6 import open_file, count_words
from pathlib import Path
TEST_FILE = Path(__file__).parent.parent / "task6_read_me.txt"

def test_open_file():
    assert isinstance(open_file(TEST_FILE), str)

    assert open_file("this/path/doesnt/exist") == None

def test_count_words():
    assert count_words("This is four words.") == 4
    assert count_words(open_file(TEST_FILE)) == 104