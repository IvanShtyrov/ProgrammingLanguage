# Запрашиваем у пользователя количество чисел в последовательности
N = int(input("Введите количество чисел: "))

# Создаем пустой список для хранения последовательности
sequence = []

# Заполняем список введенными числами
for i in range(N):
    num = int(input("Число: "))
    sequence.append(num)

# Функция для проверки, является ли последовательность симметричной
def is_symmetric(seq):
    return seq == seq[::-1]

# Инициализируем переменные для хранения минимального количества и чисел для добавления
min_additions = 0
numbers_to_add = []

# Пока последовательность не станет симметричной, добавляем числа в конец
while not is_symmetric(sequence):
    min_additions += 1
    numbers_to_add.append(sequence[-1])
    sequence.pop()

# Выводим результат
print("Последовательность:", sequence)
print("Нужно приписать чисел:", min_additions)
print("Сами числа:", numbers_to_add)
