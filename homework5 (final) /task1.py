# Определяем класс Stack для реализации стека
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)

# Определяем класс TaskManager для управления задачами
class TaskManager:
    def __init__(self):
        self.tasks = Stack()  # Инициализируем стек для хранения задач

    def new_task(self, task, priority):
        # Метод для добавления новой задачи в стек с указанным приоритетом
        self.tasks.push((priority, task))

    def remove_task(self, task):
        # Метод для удаления задачи из стека
        new_stack = Stack()  # Создаем новый стек для временного хранения задач
        while not self.tasks.is_empty():
            item = self.tasks.pop()
            if item[1] != task:  # Если задача не совпадает с удаляемой, оставляем её в новом стеке
                new_stack.push(item)
        while not new_stack.is_empty():
            self.tasks.push(new_stack.pop())  # Восстанавливаем исходный стек без удаленной задачи

    def __str__(self):
        # Метод для представления списка задач в виде строки
        sorted_tasks = sorted(self.tasks.items, key=lambda x: x[0])  # Сортировка задач по приоритету
        result = []
        for priority, task in sorted_tasks:
            result.append(f"{priority} {task}")  # Форматируем задачи в строку

        return '\n'.join(result)  # Возвращаем строки задач, разделенные переводом строки

# Пример использования
manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)

manager.remove_task("поесть")  # Удаление задачи
print(manager)
