class NativeCache:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size
        self.loaded = 0

    def hash_fun(self, key):
        hash_value = int()
        for i in range(len(key)):
            hash_value += ord(key[i])*(i+1)
        return hash_value % self.size

    def is_key(self, key):
        slot = self.hash_fun(key)
        counter = int()
        while slot < self.size:
            if self.values[slot] == key:
                return True
            else:
                if slot == self.size-1:
                    slot = 0
                else:
                    slot += 1
            counter += 1
            if counter == self.size:
                return False

    def put(self, key, value):
        # реализовтаь очистку кэша
        if self.loaded == self.size:
            min_slot = 0 # index
            min_value = self.hits[0] # take first to compare
            slot = 1 # index
            while slot < self.size:
                if self.hits[slot] <= min_value:
                    min_value = self.hits[slot]
                    min_slot = slot
                else:
                    pass
                slot += 1
            self.values[min_slot] = None
            self.slots[min_slot] = None
            self.hits[min_slot] = None
            self.loaded -= 1
        else:
            pass

        slot = self.hash_fun(key)
        while not self.values[slot] == None:
            if self.values[slot] == key:
                self.slots[slot] = value
                break
            else:
                if slot == self.size-1:
                    slot = 0
                else:
                    slot += 1
        self.values[slot] = key
        self.slots[slot] = value
        self.loaded += 1

    def get(self, key):
        # реализовать подсчёт hits
        slot = self.hash_fun(key)
        while slot < self.size:
            if self.values[slot] == key:
                self.hits[slot] += 1
                return self.slots[slot]
            else:
                if slot == self.size-1:
                    slot = 0
                else:
                    slot += 1
        return None

    def get_hit(self, key):
        # реализовать подсчёт hits
        slot = self.hash_fun(key)
        while slot < self.size:
            if self.values[slot] == key:
                return self.hits[slot]
            else:
                if slot == self.size-1:
                    slot = 0
                else:
                    slot += 1
        return None
