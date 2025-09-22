def is_leap_year(year):
    """
    Определяет, является ли год високосным.

    Args:
        year (int): Год для проверки

    Returns:
        bool: True если год високосный, False в противном случае

    Правила определения високосного года:
    1. Если год делится на 400 - високосный
    2. Если год делится на 100 - не високосный
    3. Если год делится на 4 - високосный
    4. Во всех остальных случаях - не високосный
    """
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

# чекаем этот говнокод
if __name__ == "__main__":
    # самые ненавистные годы
    test_years = [2000, 2004, 1900, 2020, 2021, 1600, 1700]

    print("Проверка високосных годов:")
    print("-" * 30)

    for year in test_years:
        result = is_leap_year(year)
        status = "високосный" if result else "не високосный"
        print(f"{year} год - {status}")

    print("\nСравнение с альтернативной версией:")
    print("-" * 40)

    for year in test_years:
        result1 = is_leap_year(year)
        result2 = is_leap_year_short(year)
        print(f"{year}: версия1={result1}, версия2={result2}, совпадают={result1 == result2}")

# за*бался печатать