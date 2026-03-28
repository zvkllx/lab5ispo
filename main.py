# main.py
from prime_checker import is_prime

# Примеры использования
print("Проверка простых чисел:")
print(f"7 - простое число? {is_prime(7)}")        # True
print(f"10 - простое число? {is_prime(10)}")      # False
print(f"2 - простое число? {is_prime(2)}")        # True
print(f"1 - простое число? {is_prime(1)}")        # False
print(f"97 - простое число? {is_prime(97)}")      # True

# Проверка нескольких чисел подряд
numbers = [1, 2, 3, 4, 5, 10, 11, 17, 20, 23]
print("\nПроверка списка чисел:")
for num in numbers:
    result = "простое" if is_prime(num) else "составное"
    print(f"{num}: {result}")