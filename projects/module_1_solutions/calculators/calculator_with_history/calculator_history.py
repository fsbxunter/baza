"""
Калькулятор с сохранением истории операций
"""

history = []


def calculate(a, op, b):
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else "Ошибка: деление на ноль!",
        '^': lambda x, y: x ** y
    }

    if op in operations:
        result = operations[op](a, b)
        history.append(f"{a} {op} {b} = {result}")
        return result
    else:
        return "Ошибка: неверный оператор!"


def show_history():
    print("\nИстория операций:")
    for i, operation in enumerate(history, 1):
        print(f"{i}. {operation}")


def main():
    print("Калькулятор с историей операций")

    while True:
        print("\nВыберите действие:")
        print("1. Выполнить вычисление")
        print("2. Показать историю")
        print("3. Очистить историю")
        print("4. Выйти")

        choice = input("Ваш выбор (1-4): ")

        if choice == '1':
            try:
                a = float(input("Первое число: "))
                op = input("Оператор (+, -, *, /, ^): ")
                b = float(input("Второе число: "))

                result = calculate(a, op, b)
                print(f"Результат: {result}")

            except ValueError:
                print("Ошибка: введите корректные числа!")

        elif choice == '2':
            if history:
                show_history()
            else:
                print("История пуста!")

        elif choice == '3':
            history.clear()
            print("История очищена!")

        elif choice == '4':
            print("До свидания!")
            break

        else:
            print("Неверный выбор!")


if __name__ == "__main__":
    main()