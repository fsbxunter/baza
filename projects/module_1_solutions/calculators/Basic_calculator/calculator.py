"""
Простой калькулятор с базовыми операциями
"""
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль!"
    return a / b

def power(a, b):
    return a ** b

def main():
    print("Добро пожаловать в простой калькулятор!")
    print("Доступные операции: +, -, *, /, ^")
    
    try:
        num1 = float(input("Введите первое число: "))
        operator = input("Введите оператор (+, -, *, /, ^): ")
        num2 = float(input("Введите второе число: "))
        
        if operator == '+':
            result = add(num1, num2)
        elif operator == '-':
            result = subtract(num1, num2)
        elif operator == '*':
            result = multiply(num1, num2)
        elif operator == '/':
            result = divide(num1, num2)
        elif operator == '^':
            result = power(num1, num2)
        else:
            result = "Ошибка: неверный оператор!"
        
        print(f"Результат: {result}")
    
    except ValueError:
        print("Ошибка: пожалуйста, введите корректные числа!")

if __name__ == "__main__":
    main()