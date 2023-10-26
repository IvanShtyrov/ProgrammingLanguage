# Создаем словарь для хранения данных о переводе оценок
score_table = {
    'A': (91, 100, 5),
    'B': (84, 90, 4),
    'C': (74, 83, 4),
    'D': (68, 73, 3),
    'E': (61, 67, 3),
    'P': (0, 60, 2)
}

# Функция для перевода числового значения в буквенное
def numeric_to_letter(score):
    for letter, (min_score, max_score, letter_value) in score_table.items():
        if min_score <= score <= max_score:
            return letter
    raise ValueError("Недопустимое числовое значение")

# Функция для перевода буквенного значения в числовое
def letter_to_numeric(letter):
    if letter in score_table:
        return score_table[letter][2]
    raise ValueError("Недопустимое буквенное значение")

# Основной цикл программы
while True:
    user_input = input("Введите оценку (число или букву): ")

    # Попытка конвертировать введенное значение из числового в буквенное
    try:
        if user_input:
            user_input = float(user_input)
            letter_grade = numeric_to_letter(user_input)
            print(f"Буквенное обозначение: {letter_grade}")
        else:
            break  # Выход из цикла при пустом вводе
    except ValueError:
        # Если возникает исключение, попробуем выполнить обратное преобразование
        try:
            letter_grade = user_input.upper()
            numeric_grade = letter_to_numeric(letter_grade)
            print(f"Числовой эквивалент: {numeric_grade}")
        except ValueError:
            print("Введенное значение не является допустимым")

print("Программа завершена")
