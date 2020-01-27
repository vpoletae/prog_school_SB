import unittest
from Bloom import BloomFilter

class Test_Bloom(unittest.TestCase):

    def test_bloom(self):
        bloom = BloomFilter(10)
        bloom.add('0123456789')
        bloom.add('1234567890')
        bloom.add('2345678901')
        bloom.add('3456789012')
        bloom.add('4567890123')
        bloom.add('5678901234')
        bloom.add('6789012345')
        bloom.add('7890123456')
        bloom.add('8901234567')
        bloom.add('9012345678')
        self.assertEqual(bloom.is_value('0123456789'), True)
        self.assertEqual(bloom.is_value('1234567890'), True)
        self.assertEqual(bloom.is_value('2345678901'), True)
        self.assertEqual(bloom.is_value('3456789012'), True)
        self.assertEqual(bloom.is_value('4567890123'), True)
        self.assertEqual(bloom.is_value('5678901234'), True)
        self.assertEqual(bloom.is_value('6789012345'), True)
        self.assertEqual(bloom.is_value('7890123456'), True)
        self.assertEqual(bloom.is_value('8901234567'), True)
        self.assertEqual(bloom.is_value('9012345678'), True)
        self.assertEqual(bloom.is_value('012345678'), False)
        self.assertEqual(bloom.is_value('cat'), False)
        self.assertEqual(bloom.is_value('0123456788'), False)

if __name__ == '__main__':
    unittest.main()
