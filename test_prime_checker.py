import unittest
from prime_checker import is_prime

class TestPrimeChecker(unittest.TestCase):
    
    def test_prime_numbers(self):
        """Проверка простых чисел"""
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        for prime in primes:
            with self.subTest(number=prime):
                self.assertTrue(is_prime(prime), f"{prime} должно быть простым")
    
    def test_not_prime_numbers(self):
        """Проверка составных чисел"""
        not_primes = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 49, 100, 121, 143]
        for not_prime in not_primes:
            with self.subTest(number=not_prime):
                self.assertFalse(is_prime(not_prime), f"{not_prime} не должно быть простым")
    
    def test_numbers_less_than_or_equal_to_one(self):
        """Проверка чисел ≤ 1 (не простые)"""
        not_primes = [0, 1, -1, -2, -5, -10, -100]
        for num in not_primes:
            with self.subTest(number=num):
                self.assertFalse(is_prime(num), f"{num} не должно быть простым")
    
    def test_large_prime(self):
        """Проверка большого простого числа"""
        self.assertTrue(is_prime(999983))  # Известное простое число
    
    def test_large_composite(self):
        """Проверка большого составного числа"""
        self.assertFalse(is_prime(1000000))  # 1 000 000 - составное
    
    def test_square_numbers(self):
        """Проверка квадратов чисел (не простые)"""
        squares = [4, 9, 16, 25, 36, 49, 64, 81, 100]
        for square in squares:
            with self.subTest(number=square):
                self.assertFalse(is_prime(square), f"{square} (квадрат) не должно быть простым")
    
    def test_even_numbers_greater_than_two(self):
        """Проверка чётных чисел > 2 (не простые)"""
        for even in range(4, 100, 2):
            self.assertFalse(is_prime(even), f"{even} (чётное) не должно быть простым")
    
    def test_invalid_input_type(self):
        """Проверка некорректных типов входных данных"""
        with self.assertRaises(TypeError):
            is_prime("5")
        with self.assertRaises(TypeError):
            is_prime(3.14)
        with self.assertRaises(TypeError):
            is_prime([2])
        with self.assertRaises(TypeError):
            is_prime(None)

if __name__ == "__main__":
    unittest.main()