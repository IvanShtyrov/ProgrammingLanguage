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
            self.add_hour()  # При добавлении минуты, если достигнута 59 минута, увеличиваем час

    def add_second(self):
        """
        Метод для добавления одной секунды к текущему времени.
        """
        if self.seconds < 59:
            self.seconds += 1
        else:
            self.seconds = 0
            self.add_minute()  # При добавлении секунды, если достигнута 59 секунда, увеличиваем минуту

    def __str__(self):
        """
        Метод для строкового представления времени в формате "чч:мм:сс".
        """
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

# Пример использования:
clock = Clock(10, 30, 45)
print("Текущее время:", clock)

clock.add_hour()
print("Добавили час:", clock)

clock.add_minute()
print("Добавили минуту:", clock)

clock.add_second()
print("Добавили секунду:", clock)
