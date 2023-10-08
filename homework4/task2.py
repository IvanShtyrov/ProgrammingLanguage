class Rectangle:
    def __init__(self, lower_left, upper_right):
        """
        Конструктор класса Rectangle.

        Args:
            lower_left (Point): Экземпляр класса Point, представляющий левый нижний угол.
            upper_right (Point): Экземпляр класса Point, представляющий правый верхний угол.
        """
        self.lower_left = lower_left
        self.upper_right = upper_right

    def area(self):
        """
        Метод для вычисления площади прямоугольника.

        Returns:
            float: Площадь прямоугольника.
        """
        width = self.upper_right.x - self.lower_left.x
        height = self.upper_right.y - self.lower_left.y
        return width * height

    def perimeter(self):
        """
        Метод для вычисления периметра прямоугольника.

        Returns:
            float: Периметр прямоугольника.
        """
        width = self.upper_right.x - self.lower_left.x
        height = self.upper_right.y - self.lower_left.y
        return 2 * (width + height)

# Пример использования:
point1 = Point(1.0, 2.0)  # Левый нижний угол
point2 = Point(4.0, 5.0)  # Правый верхний угол
rectangle = Rectangle(point1, point2)

print(f"Площадь прямоугольника: {rectangle.area()}")
print(f"Периметр прямоугольника: {rectangle.perimeter()}")
