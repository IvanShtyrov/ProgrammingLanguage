# Запрос двузначного числа
two_digit_number = int(input("Введите двузначное число: "))

# Разделяем число на десятки и единицы
tens_digit = two_digit_number // 10
ones_digit = two_digit_number % 10

# Вычисляем сумму и произведение цифр
sum_of_digits = tens_digit + ones_digit
product_of_digits = tens_digit * ones_digit

# Выводим результат для двузначного числа
print(f"Сумма цифр: {sum_of_digits}")
print(f"Произведение цифр: {product_of_digits}")

# Запрос трехзначного числа
three_digit_number = int(input("Введите трехзначное число: "))
