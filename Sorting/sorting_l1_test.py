from sorting_l1 import *
import unittest

class Test_sorting(unittest.TestCase):

    def test_selection(self):
        array = [4,3,1,2]
        for i in range(len(array)):
            array = SelectionSortStep(array, i)
        self.assertEqual(array, [1, 2, 3, 4])
        self.assertEqual(len(array), 4)
        # empty
        array = []
        for i in range(len(array)):
            array = SelectionSortStep(array, i)
        self.assertEqual(array, [])
        self.assertEqual(len(array), 0)
        # Unit
        array = [1]
        for i in range(len(array)):
            array = SelectionSortStep(array, i)
        self.assertEqual(array, [1])
        self.assertEqual(len(array), 1)
        # two
        array = [2, 1]
        for i in range(len(array)):
            array = SelectionSortStep(array, i)
        self.assertEqual(array, [1, 2])
        self.assertEqual(len(array), 2)
        # two sorted
        array = [1, 2, 3, 4]
        for i in range(len(array)):
            array = SelectionSortStep(array, i)
        self.assertEqual(array, [1, 2, 3, 4])
        self.assertEqual(len(array), 4)

    def test_bubble(self):
        array = [4,3,1,2]
        self.assertEqual(BubbleSortStep(array), False)
        self.assertEqual(array, [3, 1, 2, 4])
        self.assertEqual(BubbleSortStep(array), False)
        self.assertEqual(array, [1, 2, 3, 4])
        self.assertEqual(BubbleSortStep(array), True)
        # empty
        array = []
        self.assertEqual(BubbleSortStep(array), True)
        self.assertEqual(array, [])
        # unit
        array = [1]
        self.assertEqual(BubbleSortStep(array), True)
        self.assertEqual(array, [1])
        # two
        array = [1, 3]
        self.assertEqual(BubbleSortStep(array), True)
        self.assertEqual(array, [1, 3])

if __name__ == '__main__':
    unittest.main()
