class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
        # в качестве key поступают строки!
        # всегда возвращает корректный индекс слота
        hash_value = int()
        for i in range(len(key)):
            hash_value += ord(key[i])*(i+1)
        return hash_value % self.size

    def is_key(self, key):
        # возвращает True если ключ имеется,
        # иначе False
        slot = self.hash_fun(key)
        while slot < self.size:
            if self.values[slot] == key:
                return True
            else:
                slot += 1
        return False

    def put(self, key, value):
        # гарантированно записываем
        # значение value по ключу key
        slot = self.hash_fun(key)
        while not self.values[slot] == None:
            if self.values[slot] == key:
                self.slots[slot] = value
                break
            else:
                slot += 1
        self.values[slot] = key
        self.slots[slot] = value

    def get(self, key):
        # возвращает value для key,
        # или None если ключ не найден
        slot = self.hash_fun(key)
        while slot < self.size:
            if self.values[slot] == key:
                return self.slots[slot]
            else:
                slot += 1
        return None
