# Ввод количества коньков
num_skates = int(input("Кол-во коньков: "))

# Создание списка размеров коньков
skate_sizes = []
for i in range(num_skates):
    size = int(input(f"Размер {i+1}-й пары: "))
    skate_sizes.append(size)

# Ввод количества людей
num_people = int(input("Кол-во людей: "))

# Создание списка размеров ног людей
foot_sizes = []
for i in range(num_people):
    size = int(input(f"Размер ноги {i+1}-го человека: "))
    foot_sizes.append(size)

# Сортировка списков в порядке убывания размеров
skate_sizes.sort(reverse=True)
foot_sizes.sort(reverse=True)

# Инициализация счетчика совпадений размеров
matches = 0

# Перебор размеров коньков и ног людей для определения совпадений
for skate_size in skate_sizes:
    for i, foot_size in enumerate(foot_sizes):
        if foot_size >= skate_size:
            matches += 1
            # Удаление размера ноги, чтобы избежать повторного использования
            del foot_sizes[i]
            break  # Переходим к следующей паре коньков

# Вывод результата
print("Наибольшее кол-во людей, которые могут взять ролики:", matches)
