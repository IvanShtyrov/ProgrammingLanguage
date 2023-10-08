class Clock:
    def __init__(self, hours=0, minutes=0, seconds=0):
        """
        Конструктор класса Clock.

        Args:
            hours (int): Начальное значение часов (по умолчанию 0).
            minutes (int): Начальное значение минут (по умолчанию 0).
            seconds (int): Начальное значение секунд (по умолчанию 0).
        """
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def add_hour(self):
        """
        Метод для добавления одного часа к текущему времени.
        """
        if self.hours < 23:
            self.hours += 1
        else:
            self.hours = 0

    def add_minute(self):
        """
        Метод для добавления одной минуты к текущему времени.
        """
        if self.minutes < 59:
            self.minutes += 1
        else:
            self.minutes = 0
            self.add_hour()

    def add_second(self):
        """
        Метод для добавления одной секунды к текущему времени.
        """
        if self.seconds < 59:
            self.seconds += 1
        else:
            self.seconds = 0
            self.add_minute()

    def __str__(self):
        """
        Метод для строкового представления времени в формате "чч:мм:сс".
        """
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def __add__(self, other):
        """
        Метод для перегрузки оператора +, позволяющий складывать два объекта Clock.

        Args:
            other (Clock): Другой объект Clock, который нужно сложить с текущим.

        Returns:
            Clock: Новый объект Clock с результатом сложения времени.
        """
        total_seconds_self = self.hours * 3600 + self.minutes * 60 + self.seconds
        total_seconds_other = other.hours * 3600 + other.minutes * 60 + other.seconds

        total_seconds_result = total_seconds_self + total_seconds_other

        hours_result = total_seconds_result // 3600
        minutes_result = (total_seconds_result % 3600) // 60
        seconds_result = total_seconds_result % 60

        return Clock(hours_result, minutes_result, seconds_result)

# Пример использования:
clock1 = Clock(10, 30, 45)
clock2 = Clock(3, 15, 20)

print("Часы 1:", clock1)
print("Часы 2:", clock2)

sum_clock = clock1 + clock2
print("Сумма часов 1 и 2:", sum_clock)
