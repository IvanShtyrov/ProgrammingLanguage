# Получаем предложение от пользователя
input_sentence = input("Введите предложение: ")

# Инициализируем пустой словарь для хранения статистики символов
character_count = {}

# Приводим предложение к нижнему регистру, чтобы не учитывать регистр букв
input_sentence = input_sentence.lower()

# Проходимся по каждому символу в предложении
for char in input_sentence:
    # Проверяем, является ли символ буквой
    if char.isalpha():
        # Если символ уже встречался, увеличиваем счетчик на 1
        if char in character_count:
            character_count[char] += 1
        # Если символ встречается впервые, добавляем его в словарь
        else:
            character_count[char] = 1

# Выводим статистику символов
for char, count in character_count.items():
    print(f"{char} = {count}")
