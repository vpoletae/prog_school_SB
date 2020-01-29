class PowerSet:
    def __init__(self):
        self.slots = []

    def size(self):
        # количество элементов в множестве
        return len(self.slots)

    def put(self, value):
        # всегда срабатывает
        if value in self.slots:
            pass
        else:
            self.slots.append(value)

    def get(self, value):
        # возвращает True если value имеется в множестве,
        # иначе False
        if value in self.slots:
            return True
        else:
            return False

    def remove(self, value):
        # возвращает True если value удалено
        # иначе False
        if value in self.slots:
            self.slots.remove(value)
            return True
        else:
            return False

    def intersection(self, set2):
        # пересечение текущего множества и set2
        intersected = PowerSet()
        for value in self.slots:
            if value in set2.slots:
                intersected.slots.append(value)
            else:
                pass
        return intersected

    def union(self, set2):
        # объединение текущего множества и set2
        united = self
        for value in set2.slots:
            if value in self.slots:
                pass
            else:
                united.slots.append(value)
        return united


    def difference(self, set2):
        # разница текущего множества и set2
        deducted = self
        for value in set2.slots:
            if value in self.slots:
                deducted.slots.remove(value)
            else:
                pass
        return deducted

    def issubset(self, set2):
        # возвращает True, если set2 есть
        # подмножество текущего множества,
        # иначе False
        diff_set = set2.difference(self)
        if diff_set.size() == 0:
            return True
        else:
            return False
