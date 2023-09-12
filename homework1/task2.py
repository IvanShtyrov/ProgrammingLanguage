import math
# Запрос для ввода двух целых чисел
num1 = int(input("Введите первое целое число: "))
num2 = int(input("Введите второе целое число: "))

# Операции
addition_result = num1 + num2
print(f"Сложение: {addition_result}")
substration_result = num1 - num2
print(f"Вычитание: {substration_result}")
multiplication_result = num1 * num2
print(f"Умножение: {multiplication_result}")
division_result = num1 / num2
print(f"Деление: {division_result}")
floor_division_result = num1 // num2
print(f"Целочисленное деление: {floor_division_result}")
modulus_result = num1 % num2
print(f"Остаток от деления: {modulus_result}")
exponentiation_result = num1 ** num2
print(f"Возведение в степень: {exponentiation_result}")
log10_result = math.log10(num1)
print(f"Логарифм по основанию 10 от первого числа: {round(log10_result,2)}")
# Операции сравнения
less_than_result = num1 < num2
print(f"Меньше чем: {less_than_result}")
less_equal_result = num1 <= num2
print(f"Меньше или равно: {less_equal_result}")
greater_than_result = num1 > num2
print(f"Больше чем: {greater_than_result}")
greater_equal_result = num1 >= num2
print(f"Больше или равно: {greater_equal_result}")
not_equal_result = num1 != num2
print(f"Не равно: {not_equal_result}")
equal_result = num1 == num2
print(f"Равно: {equal_result}")
