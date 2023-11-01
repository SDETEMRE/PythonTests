import numbers


def value() -> int:
    return 40


print(value())


def calculate(num1: numbers, num2: numbers, operator: str) -> numbers:
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        print('Invalid operator')
        return 0


print(calculate(15, 3, '/'))
print(calculate(33, 7, '='))
