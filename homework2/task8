def last_person_standing(N, K):
    # Создаем список людей от 1 до N
    people = list(range(1, N + 1))

    # Индекс текущего человека, с которого начнется счет
    current_index = 0

    # Пока в круге остается больше одного человека
    while len(people) > 1:
        # Вычисляем индекс человека, который будет выбывать
        current_index = (current_index + K - 1) % len(people)

        # Выводим информацию о выбывшем человеке
        print(f"Выбывает человек под номером {people[current_index]}")

        # Удаляем выбывшего человека из списка
        del people[current_index]

    # Остался последний человек
    return people[0]


# Ввод данных
N = int(input("Кол-во человек: "))
K = int(input("Какое число в считалке? "))

# Вызов функции и вывод результата
result = last_person_standing(N, K)
print(f"\nОстался человек под номером {result}")
