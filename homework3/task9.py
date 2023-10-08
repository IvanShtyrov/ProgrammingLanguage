# Функция для преобразования числа из произвольной системы счисления в десятичную
def from_base_to_decimal(number, base):
    decimal_number = 0
    for digit in number:
        if digit.isdigit():
            digit_value = int(digit)
        else:
            digit_value = ord(digit.upper()) - ord('A') + 10
        decimal_number = decimal_number * base + digit_value
    return decimal_number

# Функция для преобразования числа из десятичной системы в произвольную
def from_decimal_to_base(decimal_number, target_base):
    if decimal_number == 0:
        return '0'
    result = ''
    while decimal_number > 0:
        remainder = decimal_number % target_base
        if remainder < 10:
            result = str(remainder) + result
        else:
            result = chr(ord('A') + remainder - 10) + result
        decimal_number //= target_base
    return result

# Основная программа
try:
    source_base = int(input("Введите исходную систему счисления (от 2 до 16): "))
    target_base = int(input("Введите целевую систему счисления (от 2 до 16): "))
    if 2 <= source_base <= 16 and 2 <= target_base <= 16:
        number = input("Введите число для преобразования: ").upper()
        decimal_number = from_base_to_decimal(number, source_base)
        result = from_decimal_to_base(decimal_number, target_base)
        print(f"Результат преобразования: {result}")
    else:
        print("Ошибка: Система счисления должна быть от 2 до 16.")
except ValueError:
    print("Ошибка: Введите корректное число.")
