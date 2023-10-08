import math

# Функция для вычисления НОК
def find_lcm(a, b):
    return a * b // math.gcd(a, b)

# Функция для вычисления НОД
def find_gcd(a, b):
    return math.gcd(a, b)

# Список чисел
numbers = [12, 18, 24]

# Инициализируем начальные значения НОК и НОД
lcm_result = numbers[0]
gcd_result = numbers[0]

# Проходим по списку чисел и обновляем НОК и НОД
for num in numbers[1:]:
    lcm_result = find_lcm(lcm_result, num)
    gcd_result = find_gcd(gcd_result, num)

# Выводим результат
print("НОК:", lcm_result)
print("НОД:", gcd_result)
