"""
Конвертер единиц измерения
"""


def length_converter(value, from_unit, to_unit):
    units = {
        'm': 1,
        'km': 1000,
        'cm': 0.01,
        'mm': 0.001,
        'mile': 1609.34,
        'yard': 0.9144,
        'foot': 0.3048,
        'inch': 0.0254
    }

    meters = value * units[from_unit]
    return meters / units[to_unit]


def weight_converter(value, from_unit, to_unit):
    units = {
        'kg': 1,
        'g': 0.001,
        'mg': 0.000001,
        'lb': 0.453592,
        'oz': 0.0283495
    }

    kg = value * units[from_unit]
    return kg / units[to_unit]


def temperature_converter(value, from_unit, to_unit):
    if from_unit == 'C':
        if to_unit == 'F':
            return (value * 9 / 5) + 32
        elif to_unit == 'K':
            return value + 273.15
    elif from_unit == 'F':
        if to_unit == 'C':
            return (value - 32) * 5 / 9
        elif to_unit == 'K':
            return (value - 32) * 5 / 9 + 273.15
    elif from_unit == 'K':
        if to_unit == 'C':
            return value - 273.15
        elif to_unit == 'F':
            return (value - 273.15) * 9 / 5 + 32

    return value


def main():
    print("Конвертер единиц измерения")

    categories = {
        '1': ('Длина', length_converter,
              ['m', 'km', 'cm', 'mm', 'mile', 'yard', 'foot', 'inch']),
        '2': ('Масса', weight_converter,
              ['kg', 'g', 'mg', 'lb', 'oz']),
        '3': ('Температура', temperature_converter,
              ['C', 'F', 'K'])
    }

    while True:
        print("\nВыберите категорию:")
        for key, (name, _, _) in categories.items():
            print(f"{key}. {name}")
        print("4. Выйти")

        choice = input("Ваш выбор (1-4): ")

        if choice == '4':
            print("До свидания!")
            break

        if choice not in categories:
            print("Неверный выбор!")
            continue

        category_name, converter_func, units = categories[choice]

        print(f"\n{category_name}: доступные единицы измерения: {', '.join(units)}")

        try:
            value = float(input("Введите значение: "))
            from_unit = input("Из единицы: ").strip()
            to_unit = input("В единицы: ").strip()

            if from_unit not in units or to_unit not in units:
                print("Ошибка: неверные единицы измерения!")
                continue

            result = converter_func(value, from_unit, to_unit)
            print(f"{value} {from_unit} = {result:.4f} {to_unit}")

        except ValueError:
            print("Ошибка: введите корректное числовое значение!")


if __name__ == "__main__":
    main()