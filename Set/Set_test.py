import unittest
from Set_list_corr import PowerSet
import random

class Test_Set(unittest.TestCase):

    def test_put(self):
        set = PowerSet()
        self.assertEqual(set.size(), 0)
        self.assertEqual(set.get('cat'), False)
        set.put('cat')
        set.put('dog')
        set.put('bird')
        self.assertEqual(set.size(), 3)
        self.assertEqual(set.get('cat'), True)
        self.assertEqual(set.get('dog'), True)
        self.assertEqual(set.get('bird'), True)
        set.put('bird')
        self.assertEqual(set.size(), 3)
        self.assertEqual(set.get('bear'), False)

    def test_remove(self):
        set = PowerSet()
        set.put('cat')
        set.put('dog')
        set.put('bird')
        set.remove('cat')
        self.assertEqual(set.size(), 2)
        self.assertEqual(set.get('cat'), False)
        set.remove('dog')
        self.assertEqual(set.size(), 1)
        self.assertEqual(set.get('dog'), False)
        set.remove('bird')
        self.assertEqual(set.size(), 0)
        self.assertEqual(set.get('bird'), False)
        self.assertEqual(set.remove('bear'), False)
        self.assertEqual(set.size(), 0)

    def test_empty_empty_intersection(self):
        set1 = PowerSet()
        set2 = PowerSet()
        set_test = PowerSet()
        set_new = set1.intersection(set2)
        self.assertEqual(set_new.slots, set_test.slots)

    def test_intersection_not_empty(self):
        set1 = PowerSet()
        set1.put('cat')
        set1.put('dog')
        set1.put('bird')
        set2 = PowerSet()
        set2.put('cat')
        set2.put('dog')
        set2.put('bird')
        set_test = PowerSet()
        set_test.put('cat')
        set_test.put('dog')
        set_test.put('bird')
        set_new = set1.intersection(set2)
        self.assertEqual(set_new.slots, set_test.slots)

    def test_intersection_empty(self):
        set1 = PowerSet()
        set1.put('cat')
        set1.put('dog')
        set1.put('bird')
        set2 = PowerSet()
        set2.put('bear')
        set2.put('dragon')
        set2.put('fly')
        set_test = PowerSet()
        set_new = set1.intersection(set2)
        self.assertEqual(set_new.slots, set_test.slots)

    def test_intersection_empty_v2(self):
        set1 = PowerSet()
        for i in range(20000):
            set1.put('cat')
        set2 = PowerSet()
        for i in range(20000):
            set1.put('dog')
        set_test = PowerSet()
        set_new = set1.intersection(set2)
        self.assertEqual(set_new.slots, set_test.slots)

    def test_empty_empty_union(self):
        set1 = PowerSet()
        set2 = PowerSet()
        set_test = PowerSet()
        set_new = set1.union(set2)
        self.assertEqual(set_new.slots, set_test.slots)

    def test_union_empty(self):
        set1 = PowerSet()
        set1.put('cat')
        set1.put('dog')
        set1.put('bird')
        set2 = PowerSet()
        set_test = PowerSet()
        set_test.put('cat')
        set_test.put('dog')
        set_test.put('bird')
        set_new = set1.union(set2)
        self.assertEqual(set_new.slots, set_test.slots)

    def test_union_not_empty(self):
        set1 = PowerSet()
        set1.put('cat')
        set1.put('dog')
        set1.put('bird')
        set2 = PowerSet()
        set2.put('bear')
        set2.put('dragon')
        set2.put('fly')
        set_new = set1.union(set2)
        self.assertEqual(set_new.get('cat'), True)
        self.assertEqual(set_new.get('dog'), True)
        self.assertEqual(set_new.get('bird'), True)
        self.assertEqual(set_new.get('bear'), True)
        self.assertEqual(set_new.get('dragon'), True)
        self.assertEqual(set_new.get('fly'), True)

    def test_empty_empty_difference(self):
        set1 = PowerSet()
        set2 = PowerSet()
        set_test = PowerSet()
        set_new = set1.difference(set2)
        self.assertEqual(set_new.slots, set_test.slots)

    # def test_diference_empty(self):
    #     set1 = PowerSet()
    #     set1.put('cat')
    #     set1.put('dog')
    #     set1.put('bird')
    #     for i in range(19997):
    #         set1.put('cat')
    #     set2 = PowerSet()
    #     set2.put('cat')
    #     set2.put('dog')
    #     set2.put('bird')
    #     for i in range(19997):
    #         set1.put('cat')
    #     set_new = set1.difference(set2)
    #     set_test = PowerSet()
    #     self.assertEqual(set_new.size(), 0)
    #     self.assertEqual(set_new.slots, set_test.slots)

    # def test_difference_not_empty(self):
    #     set1 = PowerSet()
    #     set1.put('cat')
    #     set1.put('dog')
    #     set1.put('bird')
    #     for i in range(19997):
    #         set1.put(random.randrange(1, 20000))
    #     set2 = PowerSet()
    #     set2.put('cat')
    #     for i in range(19999):
    #         set1.put(random.randrange(1, 20000))
    #     set_new = set1.difference(set2)
    #     self.assertEqual(set_new.get('cat'), False)
    #     self.assertEqual(set_new.get('dog'), True)
    #     self.assertEqual(set_new.get('bird'), True)
    #     # self.assertEqual(set_new.size(), 2)
    #     set3 = PowerSet()
    #     set3.put('dragon')
    #     self.assertEqual(set_new.get('dragon'), False)
    #     # self.assertEqual(set_new.size(), 2)

    def test_empty_empty_subset(self):
        set1 = PowerSet()
        set2 = PowerSet()
        self.assertEqual(set1.issubset(set2), True)

    def test_issubset_all_set(self):
        set1 = PowerSet()
        set1.put('cat')
        set1.put('dog')
        set1.put('bird')
        for i in range(19997):
            set1.put('cat')
        set2 = PowerSet()
        set2.put('cat')
        set2.put('dog')
        set2.put('bird')
        for i in range(19997):
            set1.put('cat')
        self.assertEqual(set1.issubset(set2), True)

    def test_issubset_all_param(self):
        set1 = PowerSet()
        set1.put('cat')
        set1.put('dog')
        set1.put('bird')
        for i in range(19997):
            set1.put('cat')
        set2 = PowerSet()
        set2.put('cat')
        set2.put('dog')
        set2.put('bird')
        for i in range(19997):
            set1.put('cat')
        self.assertEqual(set2.issubset(set1), True)

    def test_issubset_not_all_set(self):
        set1 = PowerSet()
        set1.put('cat')
        set1.put('dog')
        set1.put('bird')
        for i in range(19997):
            set1.put('cat')
        set2 = PowerSet()
        set2.put('cat')
        set2.put('dog')
        set2.put('dragon')
        for i in range(19997):
            set1.put('cat')
        self.assertEqual(set1.issubset(set2), False)

if __name__ == '__main__':
    unittest.main()
