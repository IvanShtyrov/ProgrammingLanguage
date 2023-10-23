# Создаем словарь для хранения кэшированных результатов
fib_cache = {}

# Создаем декоратор, который кэширует результаты
def memoize(func):
    def wrapper(*args):
        if args not in fib_cache:  # Проверяем, есть ли результат в кэше
            fib_cache[args] = func(*args)  # Если нет, вычисляем результат и сохраняем
        return fib_cache[args]  # Возвращаем результат из кэша
    return wrapper

# Применяем декоратор к функции для вычисления чисел Фибоначчи
@memoize
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Теперь можно вызывать функцию fibonacci с любыми аргументами, и результаты будут кэшированы

# Примеры использования:
result = fibonacci(10)
print(result)  # Выведет 55

result = fibonacci(5)
print(result)  # Выведет 5, так как результат уже кэширован
