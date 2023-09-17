# Изначальный список гостей
guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
# Максимальное количество гостей на вечеринке
max_guests = 6


# Функция для вывода текущего списка гостей и их количества
def print_guests():
    print(f"Сейчас на вечеринке {len(guests)} человек: {guests}")


# Начальное сообщение
print_guests()

# Цикл для взаимодействия с пользователем
while True:
    action = input("Гость пришёл или ушёл? ").strip().lower()

    # Если пользователь ввел "пора спать", завершаем программу
    if action == "пора спать":
        print("Вечеринка закончилась, все легли спать.")
        break

    if action == "пришёл":
        if len(guests) >= max_guests:
            print("Прости, но мест нет.")
        else:
            name = input("Имя гостя: ")
            guests.append(name)
            print(f"Привет, {name}!")
    elif action == "ушёл":
        name = input("Имя гостя: ")
        if name in guests:
            guests.remove(name)
            print(f"Пока, {name}!")
        else:
            print(f"{name} не было в списке гостей.")
    else:
        print("Пожалуйста, введите 'пришёл', 'ушёл' или 'пора спать'.")

    # Выводим текущий список гостей
    print_guests()
