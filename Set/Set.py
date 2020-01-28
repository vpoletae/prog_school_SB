class PowerSet:
    def __init__(self):
        self.capacity = 20000 #hardcoded
        self.step = 3
        self.slots = [None] * self.capacity
        self.load = 0

    def hash_fun(self, value):
        hash_value = int()
        for i in range(len(value)):
            hash_value += ord(value[i])*(i+1)
        return hash_value % self.capacity

    def seek_slot(self, value):
        hash_value = self.hash_fun(value)
        slot = hash_value
        if self.slots[slot] == None or self.slots[slot] == value:
            return slot
        else:
            counter = int()
            while not (self.slots[slot] == None or \
                self.slots[slot] == value):
                slot += self.step
                if slot >= self.capacity:
                    slot -= self.capacity
                if counter > self.capacity:
                    return None
                counter += 1
            return slot

    def size(self):
        # количество элементов в множестве
        size = int()
        slot = 0
        while slot < self.capacity:
            if self.slots[slot] != None:
                size += 1
            else:
                pass
            slot += 1
        return size

    def put(self, value):
        # всегда срабатывает
        slot = self.seek_slot(value)
        if slot != None:
            self.slots[slot] = value
            self.load += 1
            return slot
        else:
            return None

    def get(self, value):
        # возвращает True если value имеется в множестве,
        # иначе False
        slot = self.seek_slot(value)
        if slot != None:
            if self.slots[slot] == value:
                return True
            else:
                return False
        else:
            return False

    def remove(self, value):
        # возвращает True если value удалено
        # иначе False
        slot = self.seek_slot(value)
        if slot != None:
            if self.slots[slot] == value:
                self.slots[slot] = None
                self.load -= 1
                return True
            else:
                return False
        else:
            return False

    def intersection(self, set2):
        # пересечение текущего множества и set2
        slot = 0
        while slot < self.capacity:
            if self.slots[slot] != None:
                if set2.get(self.slots[slot]):
                    pass
                else:
                    set2.remove(self.slots[slot])
            else:
                pass
            slot += 1
        slot = 0
        while slot < set2.capacity:
            if set2.slots[slot] != None:
                if self.get(set2.slots[slot]):
                    pass
                else:
                    set2.remove(set2.slots[slot])
            else:
                pass
            slot += 1
        return set2

    def union(self, set2):
        # объединение текущего множества и set2
        slot = 0
        while slot < self.capacity:
            if self.slots[slot] != None:
                if set2.get(self.slots[slot]):
                    pass
                else:
                    set2.put(self.slots[slot])
            else:
                pass
            slot += 1
        return set2

    def difference(self, set2):
        # разница текущего множества и set2
        slot = 0
        while slot < self.capacity:
            if self.slots[slot] != None:
                if set2.get(self.slots[slot]):
                    set2.remove(self.slots[slot])
                else:
                    set2.put(self.slots[slot])
            else:
                pass
            slot += 1
        return set2

    def issubset(self, set2):
        # возвращает True, если set2 есть
        # подмножество текущего множества,
        # иначе False
        diff_set = set2.difference(self)
        if diff_set.size() == 0:
            return True
        else:
            return False
