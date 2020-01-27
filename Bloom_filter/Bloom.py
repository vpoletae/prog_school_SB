class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.bits = [0]*self.filter_len
        # создаём битовый массив длиной f_len ...

    def hash1(self, str1):
        # 17
        random_state = 17
        hash_value = int()
        for c in str1:
            code = ord(c)
            hash_value += (code*random_state)
            hash_value %= self.filter_len
        return hash_value

    def hash2(self, str1):
        # 223
        random_state = 223
        hash_value = int()
        for c in str1:
            code = ord(c)
            hash_value += (code*random_state)
            hash_value %= self.filter_len
        return hash_value

    def add(self, str1):
        hash1 = self.hash1(str1)
        hash2 = self.hash2(str1)
        self.bits[hash1] = 1
        self.bits[hash2] = 1

    def is_value(self, str1):
        # проверка, имеется ли строка str1 в фильтре
        hash1 = self.hash1(str1)
        hash2 = self.hash2(str1)
        if self.bits[hash1] == 1 and self.bits[hash2] == 1:
            return True
        else:
            return False
