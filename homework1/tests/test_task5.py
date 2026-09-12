from src.task5 import FAVORITE_BOOKS, STUDENTS, first_three_books

def test_first_three_books():
    assert first_three_books(FAVORITE_BOOKS) == ['Star Wars: Thrawn', 'Thrawn: Alliances', 'Thrawn: Treason']

def test_dict_contains_names():
    assert "Anakin Skywalker" in STUDENTS
    assert "Obi-Wan Kenobi" in STUDENTS
    assert "Mace Windu" in STUDENTS

def test_dict_contains_correct_ID():
    assert STUDENTS["Anakin Skywalker"] == 192837
    assert STUDENTS["Obi-Wan Kenobi"] == 294389
    assert STUDENTS["Mace Windu"] == 183018