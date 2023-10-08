class DecimalCounter:
    def __init__(self):
        """
        Конструктор класса DecimalCounter.

        Инициализирует внутреннее значение счётчика на 0.
        """
        self.value = 0

    def increment(self):
        """
        Метод для увеличения значения счётчика на 1.
        """
        self.value += 1

    def decrement(self):
        """
        Метод для уменьшения значения счётчика на 1, если текущее значение больше 0.
        """
        if self.value > 0:
            self.value -= 1

    def get_counter(self):
        """
        Метод для получения текущего значения счётчика.

        Returns:
            int: Текущее значение счётчика.
        """
        return self.value

# Пример использования:
counter = DecimalCounter()

print(f"Текущее значение счётчика: {counter.get_counter()}")

counter.increment()
print(f"Увеличили счётчик: {counter.get_counter()}")

counter.increment()
print(f"Увеличили счётчик: {counter.get_counter()}")

counter.decrement()
print(f"Уменьшили счётчик: {counter.get_counter()}")

counter.decrement()
print(f"Уменьшили счётчик: {counter.get_counter()}")
