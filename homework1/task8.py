a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
print(a, b)

# Используем XOR для обмена значениями
a = a ^ b
b = a ^ b
a = a ^ b

print(a, b)
