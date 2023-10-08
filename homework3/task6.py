def sort_numbers(*args):
    # Создаем два пустых списка для отрицательных и неотрицательных чисел.
    negative_numbers = []
    non_negative_numbers = []

    # Перебираем все аргументы, переданные в функцию.
    for num in args:
        if num < 0:
            # Если число отрицательное, добавляем его в список отрицательных чисел.
            negative_numbers.append(num)
        else:
            # Если число неотрицательное, добавляем его в список неотрицательных чисел.
            non_negative_numbers.append(num)

    # Сортируем список отрицательных чисел по убыванию.
    negative_numbers.sort(reverse=True)
    
    # Сортируем список неотрицательных чисел по возрастанию.
    non_negative_numbers.sort()

    # Возвращаем кортеж из двух списков.
    return (negative_numbers, non_negative_numbers)

# Пример использования функции:
negatives, non_negatives = sort_numbers(5, -2, 10, -7, 3, 0)
print("Отрицательные числа:", negatives)
print("Неотрицательные числа:", non_negatives)
