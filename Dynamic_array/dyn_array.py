import ctypes

class DynArray:

    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self,i):
        if i < 0 or i > self.count: #change
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2*self.capacity)
        self.array[self.count] = itm
        self.count += 1

    def insert(self, i, itm):
        if i < 0 or i > self.count:
            raise IndexError('Index is out of bounds')
        elif i == self.count-1:
            if self.count == self.capacity:
                self.resize(2*self.capacity)
                replaced_itm = self.__getitem__(i)
                self.array[i] = itm
                self.count += 1
                self.array[self.count-1] = replaced_itm
            elif self.count < self.capacity:
                replaced_itm = self.__getitem__(i)
                self.array[i] = itm
                self.count += 1
                self.array[self.count-1] = replaced_itm
        else:
            if self.count == self.capacity:
                self.resize(2*self.capacity)
                new_array = self.make_array(self.capacity)
                for counter in range(i):
                    new_array[counter] = self.__getitem__(counter)
                for counter in range(i, self.count):
                    new_array[counter+1] = self.__getitem__(counter)
                new_array[i] = itm
                self.array = new_array
                self.count += 1
            elif self.count < self.capacity:
                new_array = self.make_array(self.capacity)
                for counter in range(i):
                    new_array[counter] = self.__getitem__(counter)
                for counter in range(i, self.count):
                    new_array[counter+1] = self.__getitem__(counter)
                new_array[i] = itm
                self.array = new_array
                self.count += 1

    def delete(self, i):
        if self.count == 0:
            raise IndexError('Index is out of bounds')
        if i < 0 or i > self.count:
            raise IndexError('Index is out of bounds')
        elif i == self.count-1:
            self.count -= 1
            if self.count < self.capacity * 0.5:
                self.resize(int(self.capacity / 1.5))
                if self.capacity < 16:
                    self.capacity = 16
                else:
                    pass
            else:
                pass
            self.resize(self.capacity)
        else:
            new_array = self.make_array(self.capacity)
            for counter in range(i):
                new_array[counter] = self.__getitem__(counter)
            for counter in range(i+1, self.count):
                new_array[counter-1] = self.__getitem__(counter)
            self.array = new_array
            self.count -= 1
            if self.count < self.capacity * 0.5:
                self.resize(int(self.capacity / 1.5))
                if self.capacity < 16:
                    self.capacity = 16
                else:
                    pass
            else:
                pass
            self.resize(self.capacity)
