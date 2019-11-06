import unittest
from Queue import Queue

class Test_Queue(unittest.TestCase):

    def test_dequeue_empty(self):
        queue = Queue()
        self.assertEqual(None, queue.dequeue())
        self.assertEqual(0, queue.size())

    def test_dequeue(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertEqual(1, queue.dequeue())
        self.assertEqual(2, queue.size())

    def test_enqueue(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        self.assertEqual(2, queue.size())
        self.assertEqual(1, queue.dequeue())
        self.assertEqual(2, queue.dequeue())
        self.assertEqual(None, queue.dequeue())
        self.assertEqual(0, queue.size())

if __name__ == '__main__':
    unittest.main()
