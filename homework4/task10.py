total = 0  # Инициализация переменной для хранения суммы

while True:
    user_input = input("Введите число (или нажмите Enter для выхода): ")

    # Проверка на пустой ввод для выхода
    if user_input == "":
        break

    try:
        number = float(user_input)  # Пробуем преобразовать введенное значение в число
        total += number  # Добавляем число к общей сумме
        print(f"Текущая сумма: {total}")
    except ValueError:
        print("Ошибка: Введите числовое значение")

print(f"Итоговая сумма: {total}")
