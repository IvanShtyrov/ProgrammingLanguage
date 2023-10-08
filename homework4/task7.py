class Herbivore:
    def __init__(self, name, hunger_threshold):
        """
        Конструктор класса Herbivore.

        Args:
            name (str): Имя травоядного животного.
            hunger_threshold (int): Порог голода, при котором животное начинает есть траву.
        """
        self.name = name
        self.hunger_threshold = hunger_threshold
        self.hunger = 0

    def eat_grass(self, grass):
        """
        Метод для травоядного животного, который позволяет ему есть траву, если испытывает голод.

        Args:
            grass (Grass): Объект класса Grass, представляющий траву.

        Returns:
            str: Сообщение о действии животного (съел траву или отказался).
        """
        if self.hunger < self.hunger_threshold:
            self.hunger += grass.nutrition
            return f"{self.name} съел траву и насытился."
        else:
            return f"{self.name} не голоден и отказывается от травы."


class Grass:
    def __init__(self, nutrition):
        """
        Конструктор класса Grass.

        Args:
            nutrition (int): Питательность травы.
        """
        self.nutrition = nutrition


# Пример использования:
grass1 = Grass(10)  # Создаем траву с питательностью 10
grass2 = Grass(5)   # Создаем траву с питательностью 5

herbivore1 = Herbivore("Зайц", hunger_threshold=15)
herbivore2 = Herbivore("Олень", hunger_threshold=12)

print(herbivore1.eat_grass(grass1))  # Зайц съел траву и насытился.
print(herbivore2.eat_grass(grass2))  # Олень не голоден и отказывается от травы.
