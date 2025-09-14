"""
Генератор случайных паролей
"""

import random
import string


def generate_password(length=12, use_digits=True, use_special_chars=True):
    """
    Генерирует случайный пароль заданной длины.

    :param length: Длина пароля (по умолчанию 12)
    :param use_digits: Включать ли цифры
    :param use_special_chars: Включать ли специальные символы
    :return: Сгенерированный пароль
    """
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits

    if use_special_chars:
        characters += string.punctuation

    if not characters:
        return "Ошибка: не выбрано ни одного набора символов!"

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def get_yes_no_input(prompt):
    """
    Запрашивает у пользователя ответ да/нет и возвращает булево значение.

    :param prompt: Подсказка для пользователя
    :return: True если ответ 'y', False если 'n'
    """
    while True:
        response = input(prompt).lower()
        if response in ['y', 'n']:
            return response == 'y'
        print("Пожалуйста, введите 'y' или 'n'.")


def main():
    print("Генератор случайных паролей")

    try:
        length = int(input("Введите длину пароля (по умолчанию 12): ") or 12)
        if length <= 0:
            print("Длина пароля должна быть положительным числом. Установлено значение по умолчанию (12).")
            length = 12
    except ValueError:
        print("Некорректный ввод. Установлено значение по умолчанию (12).")
        length = 12

    use_digits = get_yes_no_input("Включать цифры? (y/n, по умолчанию y): ")
    use_special_chars = get_yes_no_input("Включать специальные символы? (y/n, по умолчанию y): ")

    password = generate_password(length, use_digits, use_special_chars)

    print(f"\nВаш пароль: {password}")


if __name__ == "__main__":
    main()