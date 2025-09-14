"""
Игра 'Угадай число' - компьютер загадывает число, а игрок пытается его угадать
"""

import random


def play_game(min_num=1, max_num=100, max_attempts=None):
    """
    Основная функция игры

    Args:
        min_num (int): Минимальное число в диапазоне
        max_num (int): Максимальное число в диапазоне
        max_attempts (int): Максимальное количество попыток (None - без ограничений)
    """
    secret_number = random.randint(min_num, max_num)
    attempts = 0
    guessed = False

    print(f"Я загадал число от {min_num} до {max_num}. Попробуй угадать!")

    if max_attempts:
        print(f"У тебя есть {max_attempts} попыток.")

    while not guessed and (max_attempts is None or attempts < max_attempts):
        try:
            guess = int(input("Твоя догадка: "))
            attempts += 1

            if guess < min_num or guess > max_num:
                print(f"Число должно быть между {min_num} и {max_num}!")
                continue

            if guess < secret_number:
                print("Загаданное число больше!")
            elif guess > secret_number:
                print("Загаданное число меньше!")
            else:
                print(f"Поздравляю! Ты угадал число {secret_number} за {attempts} попыток!")
                guessed = True

        except ValueError:
            print("Пожалуйста, введите целое число!")

    if not guessed:
        print(f"К сожалению, ты исчерпал все попытки. Загаданное число было: {secret_number}")


def select_difficulty():
    """
    Функция выбора уровня сложности

    Returns:
        tuple: (min_num, max_num, max_attempts)
    """
    print("\nВыбери уровень сложности:")
    print("1. Легкий (1-50, 10 попыток)")
    print("2. Средний (1-100, 7 попыток)")
    print("3. Сложный (1-200, 5 попыток)")
    print("4. Произвольный (сам задашь диапазон и попытки)")

    while True:
        try:
            choice = int(input("Твой выбор (1-4): "))

            if choice == 1:
                return 1, 50, 10
            elif choice == 2:
                return 1, 100, 7
            elif choice == 3:
                return 1, 200, 5
            elif choice == 4:
                min_num = int(input("Минимальное число: "))
                max_num = int(input("Максимальное число: "))
                max_attempts = int(input("Количество попыток: "))
                return min_num, max_num, max_attempts
            else:
                print("Пожалуйста, выбери от 1 до 4")

        except ValueError:
            print("Пожалуйста, введите число!")


def main():
    print("Добро пожаловать в игру 'Угадай число'!")

    while True:
        min_num, max_num, max_attempts = select_difficulty()

        play_game(min_num, max_num, max_attempts)

        play_again = input("\nХочешь сыграть еще раз? (да/нет): ").lower()
        if play_again not in ['да', 'д', 'yes', 'y']:
            print("Спасибо за игру! До свидания!")
            break


if __name__ == "__main__":
    main()