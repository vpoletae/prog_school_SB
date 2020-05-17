import unittest
from Heap import *

class Test_Heap(unittest.TestCase):

    def test_make_heap_full(self):
        array = [1, 2, 3]
        depth = 1
        heap = Heap()
        heap.MakeHeap(array, depth)
        self.assertEqual(heap.HeapArray, [3, 1, 2])

    def test_make_heap_not_full(self):
        array = [1, 2, 3, 4, 5, 6, 7]
        depth = 2
        heap = Heap()
        heap.MakeHeap(array, depth)
        self.assertEqual(heap.HeapArray, [7, 4, 6, 1, 3, 2, 5])

    def test_get_max_empty(self):
        heap = Heap()
        self.assertEqual(heap.GetMax(), -1)

    def test_get_max_one(self):
        array = [1]
        depth = 0
        heap = Heap()
        heap.MakeHeap(array, depth)
        self.assertEqual(heap.GetMax(), 1)
        self.assertEqual(heap.HeapArray, [None])
        self.assertEqual(heap.GetMax(), None)

    def test_get_max_three(self):
        array = [1, 2, 3]
        depth = 1
        heap = Heap()
        heap.MakeHeap(array, depth)
        self.assertEqual(heap.HeapArray, [3, 1, 2])
        self.assertEqual(heap.GetMax(), 3)
        self.assertEqual(heap.HeapArray, [2, 1, None])
        self.assertEqual(heap.GetMax(), 2)
        self.assertEqual(heap.HeapArray, [1, None, None])
        self.assertEqual(heap.GetMax(), 1)
        self.assertEqual(heap.HeapArray, [None, None, None])

    def test_get_max_full(self):
        array = [1, 2, 3, 4, 5, 6, 7]
        depth = 2
        heap = Heap()
        heap.MakeHeap(array, depth)
        self.assertEqual(heap.HeapArray, [7, 4, 6, 1, 3, 2, 5])
        self.assertEqual(heap.GetMax(), 7)
        self.assertEqual(heap.HeapArray, [6, 4, 5, 1, 3, 2, None])
        self.assertEqual(heap.GetMax(), 6)
        self.assertEqual(heap.HeapArray, [5, 4, 2, 1, 3, None, None])
        self.assertEqual(heap.GetMax(), 5)
        self.assertEqual(heap.HeapArray, [4, 3, 2, 1, None, None, None])
    
    def test_add(self):
        array = []
        depth = 1
        heap = Heap()
        heap.MakeHeap(array, depth)
        self.assertEqual(heap.Add(1), True)
        self.assertEqual(heap.HeapArray, [1, None, None])
        self.assertEqual(heap.Add(2), True)
        self.assertEqual(heap.HeapArray, [2, 1, None])
        self.assertEqual(heap.Add(3), True)
        self.assertEqual(heap.HeapArray, [3, 1, 2])
        self.assertEqual(heap.Add(4), False)

if __name__ == '__main__':
    unittest.main()
