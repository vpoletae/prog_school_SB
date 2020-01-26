import unittest
from Dict import NativeDictionary

class Test_Dict(unittest.TestCase):

    def test_put_new(self):
        dict = NativeDictionary(3)
        dict.put('cat', 'cat')
        dict.put('tac', 'tac')
        dict.put('bird', 'bird')
        self.assertEqual(dict.get('cat'), 'cat')
        self.assertEqual(dict.get('tac'), 'tac')
        self.assertEqual(dict.get('bird'), 'bird')
        self.assertEqual(dict.is_key('cat'), True)
        self.assertEqual(dict.is_key('tac'), True)
        self.assertEqual(dict.is_key('bird'), True)
        self.assertEqual(dict.is_key('dog'), False)

    def test_put_existing(self):
        dict = NativeDictionary(5)
        dict.put('cat', 'cat')
        dict.put('tac', 'tac')
        dict.put('bird', 'bird')
        dict.put('tac', 'dog')
        dict.put('cat', 'dragon')
        self.assertEqual(dict.get('cat'), 'dragon')
        self.assertEqual(dict.get('tac'), 'dog')
        self.assertEqual(dict.get('bird'), 'bird')
        self.assertEqual(dict.get('dragon'), None)
        self.assertEqual(dict.is_key('cat'), True)
        self.assertEqual(dict.is_key('tac'), True)
        self.assertEqual(dict.is_key('bird'), True)
        self.assertEqual(dict.is_key('dog'), False)

if __name__ == '__main__':
    unittest.main()
