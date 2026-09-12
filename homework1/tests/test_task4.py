from src.task4 import calculate_discount

def test_calculate_discount():
    assert calculate_discount(5, 10) == 4.50
    assert calculate_discount(7, 10) == 6.30
    assert calculate_discount(10, 3.5) == 9.65
    assert calculate_discount(4.99, 20.5) == 3.97
