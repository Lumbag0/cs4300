from src.task3 import is_negative, is_zero, first_10_prime, sum_to_100

class TestIsNegative:
    def test_pos_num(self):
        assert is_negative(1) is False

    def test_negative_num(self):
        assert is_negative(-1) is True

    def test_negative_float(self):
        assert is_negative(-1.5) is True

    def test_positive_float(self):
        assert is_negative(1.5) is False

    def test_zero(self):
        assert is_negative(0) is False

class TestIsZero:
    def test_zero(self):
        assert is_zero(0) is True

    def test_positive(self):
        assert is_zero(1) is False

    def test_negative(self):
        assert is_zero(-1) is False

    def test_zero_floated(self):
        assert is_zero(0.0) is True

class TestFirst10Prime:
    def test_returns_ten_primes(self):
        primes = first_10_prime()
        assert len(primes) == 10

    def test_correct_primes(self):
        assert first_10_prime() == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    def test_all_values_are_prime(self):
        for prime in first_10_prime():
            assert prime > 1
            for i in range(2, int(prime**0.5) + 1):
                assert prime % i != 0    

class TestSumTo100:
    def test_sum_matches(self):
        assert sum_to_100() == 5050