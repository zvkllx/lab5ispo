# find_primes.py
from prime_checker import is_prime

def find_primes_in_range(start, end):
    """Находит все простые числа в заданном диапазоне"""
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# Пример: найти все простые числа от 1 до 100
primes_up_to_100 = find_primes_in_range(1, 100)
print(f"Простые числа от 1 до 100:")
print(primes_up_to_100)
print(f"\nВсего найдено: {len(primes_up_to_100)} простых чисел")