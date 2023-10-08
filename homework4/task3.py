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

    def contains(self, point):
        """
        Метод для проверки, находится ли данная точка внутри прямоугольника.

        Args:
            point (Point): Экземпляр класса Point, представляющий точку.

        Returns:
            bool: True, если точка находится внутри прямоугольника, и False в противном случае.
        """
        if (self.lower_left.x <= point.x <= self.upper_right.x) and \
           (self.lower_left.y <= point.y <= self.upper_right.y):
            return True
        else:
            return False

# Пример использования:
point1 = Point(1.0, 2.0)  # Левый нижний угол
point2 = Point(4.0, 5.0)  # Правый верхний угол
rectangle = Rectangle(point1, point2)

point_inside = Point(2.0, 3.0)
point_outside = Point(5.0, 6.0)

print(f"Точка {point_inside.x},{point_inside.y} внутри прямоугольника: {rectangle.contains(point_inside)}")
print(f"Точка {point_outside.x},{point_outside.y} внутри прямоугольника: {rectangle.contains(point_outside)}")
