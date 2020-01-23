class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        # в качестве value поступают строки!
        # всегда возвращает корректный индекс слота
        hash_value = int()
        for i in range(len(value)):
            hash_value += ord(value[i])*(i+1)
        return hash_value % self.size

    def seek_slot(self, value):
        # находит индекс пустого слота для значения, или None
        hash_value = self.hash_fun(value)
        slot = hash_value
        if self.slots[slot] == None or self.slots[slot] == value:
            return slot
        else:
            counter = int()
            while not (self.slots[slot] == None or \
                self.slots[slot] == value):
                slot += self.step
                if slot >= self.size:
                    slot -= self.size
                if counter > self.size:
                    return None
                counter += 1
            return slot

    def put(self, value):
        # записываем значение по хэш-функции
        # возвращается индекс слота или None,
        # если из-за коллизий элемент не удаётся
        # разместить
        slot = self.seek_slot(value)
        if slot != None:
            self.slots[slot] = value
            return slot
        else:
            return None

    def find(self, value):
        # находит индекс слота со значением, или None
        slot = self.seek_slot(value)
        if slot != None:
            if self.slots[slot] == value:
                return slot
            else:
                return None
        else:
            return None
