class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache_dict = {}
        self.usage_order = []

    @property
    def cache(self):
        # Возвращаем самый старый элемент
        if self.usage_order:
            return self.cache_dict[self.usage_order[-1]]
        return None

    @cache.setter
    def cache(self, new_elem):
        key, value = new_elem
        if key in self.cache_dict:
            # Если ключ уже существует, обновляем его и перемещаем в начало списка использования
            self.usage_order.remove(key)
        elif len(self.cache_dict) >= self.capacity:
            # Если достигнут лимит, удаляем самый старый элемент
            oldest_key = self.usage_order.pop()
            del self.cache_dict[oldest_key]
        self.cache_dict[key] = value
        self.usage_order.insert(0, key)

    def get(self, key):
        # Получаем значение по ключу и обновляем порядок использования
        if key in self.cache_dict:
            self.usage_order.remove(key)
            self.usage_order.insert(0, key)
            return self.cache_dict[key]
        return None

    def print_cache(self):
        # Выводим текущий кэш
        print("LRU Cache:")
        for key in self.usage_order:
            print(f"{key} : {self.cache_dict[key]}")

# Создаём экземпляр класса LRU Cache с capacity = 3
cache = LRUCache(3)

# Добавляем элементы в кэш
cache.cache = ("key1", "value1")
cache.cache = ("key2", "value2")
cache.cache = ("key3", "value3")

# Выводим текущий кэш
cache.print_cache()

# Получаем значение по ключу
print(cache.get("key2"))

# Добавляем новый элемент, превышающий лимит capacity
cache.cache = ("key4", "value4")

# Выводим обновлённый кэш
cache.print_cache()
