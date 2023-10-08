class Element:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        if isinstance(other, Element):
            if self.name == "Вода" and other.name == "Воздух":
                return Element("Шторм")
            elif self.name == "Вода" and other.name == "Огонь":
                return Element("Пар")
            elif self.name == "Вода" and other.name == "Земля":
                return Element("Грязь")
            elif self.name == "Воздух" and other.name == "Огонь":
                return Element("Молния")
            elif self.name == "Воздух" and other.name == "Земля":
                return Element("Пыль")
            elif self.name == "Огонь" and other.name == "Земля":
                return Element("Лава")
            else:
                return None
        else:
            return None

    def __str__(self):
        return self.name


class MagicElement(Element):
    def __init__(self, name):
        super().__init__(name)

    def __add__(self, other):
        result = super().__add__(other)
        if result is None:
            return Element("Магический " + self.name)
        return result


# Функция для получения имени элемента от пользователя
def get_element_name():
    return input("Введите имя элемента (Вода, Воздух, Огонь, Земля, или Магия): ").strip().capitalize()


# Запрос у пользователя и вывод результата
while True:
    try:
        element_name1 = get_element_name()
        element_name2 = get_element_name()

        element1 = Element(element_name1)
        element2 = Element(element_name2)

        result = element1 + element2
        if result:
            print(f"Результат взаимодействия: {result}")
        else:
            print("Результат не определен.")
    except KeyboardInterrupt:
        print("Выход из программы.")
        break
