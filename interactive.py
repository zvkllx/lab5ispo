# interactive.py
from prime_checker import is_prime

def main():
    print("=" * 50)
    print("ПРОГРАММА ПРОВЕРКИ ПРОСТЫХ ЧИСЕЛ")
    print("=" * 50)
    
    while True:
        print("\nВведите число для проверки (или 'выход' для завершения):")
        user_input = input("> ")
        
        if user_input.lower() in ['выход', 'exit', 'quit', 'q']:
            print("До свидания!")
            break
        
        try:
            number = int(user_input)
            if is_prime(number):
                print(f"✅ {number} - ПРОСТОЕ число")
            else:
                print(f"❌ {number} - НЕ является простым числом")
                
        except ValueError:
            print("Ошибка: Пожалуйста, введите целое число")
        except TypeError:
            print("Ошибка: Некорректный ввод")

if __name__ == "__main__":
    main()