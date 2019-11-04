import unittest
from Stack import Stack

class Test_Stack(unittest.TestCase):

    def test_pop_empty(self):
        stack = Stack()
        self.assertEqual(None, stack.pop())
        self.assertEqual(0, stack.size())

    def test_pop(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(3, stack.pop())
        self.assertEqual(2, stack.size())

    def test_push(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(2, stack.size())
        self.assertEqual(2, stack.pop())
        self.assertEqual(1, stack.pop())
        self.assertEqual(None, stack.pop())

    def test_peek_empty(self):
        stack = Stack()
        self.assertEqual(None, stack.peek())
        self.assertEqual(0, stack.size())

    def test_peek(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(3, stack.peek())
        self.assertEqual(3, stack.size())

if __name__ == '__main__':
    unittest.main()
