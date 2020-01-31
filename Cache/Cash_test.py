import unittest
from Cache import NativeCache

class Test_Cashe(unittest.TestCase):

    def test_pulling(self):
        cache = NativeCache(3)
        cache.put('cat', 'cat')
        cache.put('tac', 'tac')
        cache.put('bird', 'bird')
        self.assertEqual(cache.get('cat'), 'cat')
        self.assertEqual(cache.get('tac'), 'tac')
        self.assertEqual(cache.get('bird'), 'bird')
        self.assertEqual(cache.is_key('cat'), True)
        self.assertEqual(cache.is_key('tac'), True)
        self.assertEqual(cache.is_key('bird'), True)
        self.assertEqual(cache.is_key('dog'), False)
        self.assertEqual(cache.loaded, 3)
        cache.put('dog', 'dog')
        self.assertEqual(cache.is_key('dog'), True)
        self.assertEqual(cache.loaded, 3)

    def test_count_hits(self):
        cache = NativeCache(3)
        cache.put('cat', 'cat')
        cache.put('tac', 'tac')
        cache.put('bird', 'bird')
        for i in range(10):
            cache.get('cat')
        self.assertEqual(cache.get_hit('cat'), 10)
        for i in range(100):
            cache.get('tac')
        self.assertEqual(cache.get_hit('tac'), 100)
        for i in range(1000):
            cache.get('bird')
        self.assertEqual(cache.get_hit('bird'), 1000)
        cache.put('dog', 'dog')
        self.assertEqual(cache.is_key('dog'), True)
        self.assertEqual(cache.is_key('cat'), False)
        self.assertEqual(cache.loaded, 3)

if __name__ == '__main__':
    unittest.main()
