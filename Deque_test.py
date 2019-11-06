import unittest
from Deque import Deque

class Test_Deque(unittest.TestCase):

    def test_add_front(self):
        deque = Deque()
        deque.addFront(1)
        deque.addFront(2)
        deque.addFront(3)
        self.assertEqual(3, deque.size())
        self.assertEqual(1, deque.removeFront())
        self.assertEqual(2, deque.removeFront())
        self.assertEqual(3, deque.removeFront())
    #
    def test_add_tail(self):
        deque = Deque()
        deque.addTail(1)
        deque.addTail(2)
        deque.addTail(3)
        self.assertEqual(3, deque.size())
        self.assertEqual(1, deque.removeTail())
        self.assertEqual(2, deque.removeTail())
        self.assertEqual(3, deque.removeTail())
    #
    def test_add_mix(self):
        deque = Deque()
        deque.addFront('A')
        deque.addFront('B')
        deque.addFront('C')
        deque.addTail(1)
        deque.addTail(2)
        deque.addTail(3)
        self.assertEqual(6, deque.size())
        self.assertEqual('C', deque.removeTail())
        self.assertEqual('B', deque.removeTail())
        self.assertEqual('A', deque.removeTail())
        self.assertEqual(1, deque.removeTail())
        self.assertEqual(2, deque.removeTail())
        self.assertEqual(3, deque.removeTail())
    #
    def test_remove_front_empty(self):
        deque = Deque()
        self.assertEqual(None, deque.removeFront())
        self.assertEqual(0, deque.size())
    #
    def test_remove_front_one(self):
        deque = Deque()
        deque.addTail('A')
        self.assertEqual('A', deque.removeFront())
        self.assertEqual(0, deque.size())
    #
    def test_remove_front(self):
        deque = Deque()
        deque.addFront('A')
        deque.addFront('B')
        deque.addFront('C')
        deque.addTail(1)
        deque.addTail(2)
        deque.addTail(3)
        self.assertEqual('C', deque.removeTail())
        self.assertEqual(5, deque.size())
        self.assertEqual('B', deque.removeTail())
        self.assertEqual('A', deque.removeTail())
        self.assertEqual(3, deque.removeFront())
        self.assertEqual(2, deque.removeFront())
        self.assertEqual(1, deque.removeFront())
    #
    def test_remove_tail_empty(self):
        deque = Deque()
        self.assertEqual(None, deque.removeTail())
        self.assertEqual(0, deque.size())

    def test_remove_tail_one(self):
        deque = Deque()
        deque.addFront(1)
        self.assertEqual(1, deque.removeTail())
        self.assertEqual(0, deque.size())

    def test_remove_tail(self):
        deque = Deque()
        deque.addFront('A')
        deque.addFront('B')
        deque.addFront('C')
        deque.addTail(1)
        deque.addTail(2)
        deque.addTail(3)
        self.assertEqual(3, deque.removeFront())
        self.assertEqual(5, deque.size())
        self.assertEqual('C', deque.removeTail())
        self.assertEqual('B', deque.removeTail())
        self.assertEqual('A', deque.removeTail())
        self.assertEqual(2, deque.removeFront())
        self.assertEqual(1, deque.removeFront())

if __name__ == '__main__':
    unittest.main()
