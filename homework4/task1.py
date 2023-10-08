class Point:
    def __init__(self, x, y):
        """
        Конструктор класса Point.

        Args:
            x (float): Координата x.
            y (float): Координата y.
        """
        self.x = x
        self.y = y


# Пример использования:
point1 = Point(1.0, 2.0)  # Создаем экземпляр класса Point с координатами (1.0, 2.0)
print(f"Точка 1: x={point1.x}, y={point1.y}")
