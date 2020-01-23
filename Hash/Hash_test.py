import unittest
from Hash import HashTable

class Test_Hash(unittest.TestCase):

    # def test_hash_fun(self):
    #     hash_table = HashTable(11, 3)
    #     value = 'cat'
    #     hash_value = hash_table.hash_fun(value)
    #     hash_value_tested = int()
    #     for i in range(len(value)):
    #         hash_value_tested += ord(value[i])*(i+1)
    #     self.assertEqual(hash_value, (hash_value_tested % hash_table.size))
    #     self.assertNotEqual(hash_value, hash_table.hash_fun('tac'))
    #
    # def test_seek_slot(self):
    #     hash_table = HashTable(5, 3)
    #     s1 = hash_table.seek_slot('a')
    #     s2 = hash_table.seek_slot('b')
    #     s3 = hash_table.seek_slot('c')
    #     s4 = hash_table.seek_slot('d')
    #     s5 = hash_table.seek_slot('e')
    #     s6 = hash_table.seek_slot('f')
    #     self.assertEqual(s1 != s2 != s3 != s4 != s5, True)
    #     self.assertEqual(s6 in [s1, s2, s3, s4, s5], True)
    #
    # def test_put_find(self):
    #     hash_table = HashTable(5, 3)
    #     s1 = hash_table.put('a')
    #     s2 = hash_table.put('b')
    #     s3 = hash_table.put('c')
    #     s4 = hash_table.put('d')
    #     s5 = hash_table.put('e')
    #     s6 = hash_table.put('f')
    #     print(hash_table.find('a'))
    #     print(hash_table.find('b'))
    #     print(hash_table.find('c'))
    #     print(hash_table.find('d'))
    #     print(hash_table.find('e'))
    #     print(hash_table.find('f'))
    #     self.assertEqual(hash_table.find('a') != hash_table.find('b') != hash_table.find('c') != hash_table.find('d')  != hash_table.find('e'), True)
    #     self.assertEqual(hash_table.find('f'), None)

    def test_put_find(self):
        hash_table = HashTable(5, 3)
        s1 = hash_table.put('a')
        s2 = hash_table.put('b')
        s3 = hash_table.put('b')
        s4 = hash_table.put('b')
        s5 = hash_table.put('e')
        s6 = hash_table.put('f')
        s7 = hash_table.put('g')
        self.assertEqual(hash_table.find('a') != hash_table.find('b') != hash_table.find('e') != hash_table.find('f')  != hash_table.find('g'), True)
        self.assertEqual(s2, s3)
        self.assertEqual(s3, s4)

if __name__ == '__main__':
    unittest.main()
