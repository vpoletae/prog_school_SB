import unittest
from OrderedList import Node, OrderedList, OrderedStringList

class Test_OrderedList(unittest.TestCase):
    # Sorting testing block
    def test_list_sorted_asc(self):
        val_1 = 12
        val_2 = 55
        val_3 = 100
        ordered_list = OrderedList(asc=True)
        ordered_list.add(val_1)
        ordered_list.add(val_2)
        ordered_list.add(val_3)
        self.assertEqual(val_1, ordered_list.get_all()[0].value)
        self.assertEqual(val_2, ordered_list.get_all()[1].value)
        self.assertEqual(val_3, ordered_list.get_all()[2].value)
        self.assertEqual(val_1, ordered_list.find(val_1).value)
        self.assertEqual(val_2, ordered_list.find(val_2).value)
        self.assertEqual(val_3, ordered_list.find(val_3).value)
        self.assertEqual(val_1, ordered_list.head.value)
        self.assertEqual(val_3, ordered_list.tail.value)
        self.assertEqual(3, ordered_list.len())

    def test_list_sorted_desc(self):
        val_1 = 12
        val_2 = 55
        val_3 = 100
        ordered_list = OrderedList(asc=False)
        ordered_list.add(val_1)
        ordered_list.add(val_2)
        ordered_list.add(val_3)
        self.assertEqual(val_1, ordered_list.get_all()[2].value)
        self.assertEqual(val_2, ordered_list.get_all()[1].value)
        self.assertEqual(val_3, ordered_list.get_all()[0].value)
        self.assertEqual(val_1, ordered_list.find(val_1).value)
        self.assertEqual(val_2, ordered_list.find(val_2).value)
        self.assertEqual(val_3, ordered_list.find(val_3).value)
        self.assertEqual(val_3, ordered_list.head.value)
        self.assertEqual(val_1, ordered_list.tail.value)
        self.assertEqual(3, ordered_list.len())

    def test_list_text_sorted_asc(self):
        val_1 = ' a'
        val_2 = ' с '
        val_3 = 'b '
        ordered_list = OrderedStringList(asc=True)
        ordered_list.add(val_1)
        ordered_list.add(val_2)
        ordered_list.add(val_3)
        self.assertEqual(val_1, ordered_list.get_all()[0].value)
        self.assertEqual(val_3, ordered_list.get_all()[1].value)
        self.assertEqual(val_2, ordered_list.get_all()[2].value)
        self.assertEqual(val_1, ordered_list.find(val_1).value)
        self.assertEqual(val_2, ordered_list.find(val_2).value)
        self.assertEqual(val_3, ordered_list.find(val_3).value)
        self.assertEqual(val_1, ordered_list.head.value)
        self.assertEqual(val_2, ordered_list.tail.value)
        self.assertEqual(3, ordered_list.len())

    def test_list_text_sorted_desc(self):
        val_1 = ' aaa'
        val_2 = ' aac '
        val_3 = 'aab '
        ordered_list = OrderedStringList(asc=False)
        ordered_list.add(val_1)
        ordered_list.add(val_2)
        ordered_list.add(val_3)
        self.assertEqual(val_2, ordered_list.get_all()[0].value)
        self.assertEqual(val_3, ordered_list.get_all()[1].value)
        self.assertEqual(val_1, ordered_list.get_all()[2].value)
        self.assertEqual(val_1, ordered_list.find(val_1).value)
        self.assertEqual(val_2, ordered_list.find(val_2).value)
        self.assertEqual(val_3, ordered_list.find(val_3).value)
        self.assertEqual(val_2, ordered_list.head.value)
        self.assertEqual(val_1, ordered_list.tail.value)
        self.assertEqual(3, ordered_list.len())

    # comparing testing block
    def test_compare(self):
        node_1 = Node(1)
        node_2 = Node(2)
        node_3 = Node(2)
        ordered_list = OrderedList(asc=True)
        self.assertEqual(1, ordered_list.compare(node_2, node_1))
        self.assertEqual(-1, ordered_list.compare(node_1, node_2))
        self.assertEqual(0, ordered_list.compare(node_3, node_2))

    def test_compare_string(self):
        node_1 = Node(' a')
        node_2 = Node('b')
        node_3 = Node(' ')
        node_4 = Node('a ')
        node_5 = Node('b')
        ordered_list = OrderedStringList(asc=True)
        self.assertEqual(1, ordered_list.compare(node_2, node_1))
        self.assertEqual(-1, ordered_list.compare(node_1, node_2))
        self.assertEqual(0, ordered_list.compare(node_5, node_2))
        self.assertEqual(1, ordered_list.compare(node_4, node_1))
        self.assertEqual(1, ordered_list.compare(node_1, node_3))

    # comparing testing block
    def test_find(self):
        val_1 = 12
        val_2 = 100
        val_3 = 55
        val_4 = -1
        val_5 = 55
        ordered_list = OrderedList(asc=True)
        ordered_list.add(val_1)
        ordered_list.add(val_2)
        ordered_list.add(val_3)
        ordered_list.add(val_4)
        ordered_list.add(val_5)
        self.assertEqual(val_4, ordered_list.get_all()[0].value)
        self.assertEqual(val_1, ordered_list.get_all()[1].value)
        self.assertEqual(val_3, ordered_list.get_all()[2].value)
        self.assertEqual(val_5, ordered_list.get_all()[3].value)
        self.assertEqual(val_2, ordered_list.get_all()[4].value)
        self.assertEqual(val_1, ordered_list.find(val_1).value)
        self.assertEqual(val_2, ordered_list.find(val_2).value)
        self.assertEqual(val_3, ordered_list.find(val_3).value)
        self.assertEqual(val_4, ordered_list.find(val_4).value)
        self.assertEqual(val_5, ordered_list.find(val_5).value)
        self.assertEqual(None, ordered_list.find(15))

    def test_find_string(self):
        val_1 = ' '
        val_2 = ' a'
        val_3 = ' a '
        val_4 = '-14629'
        val_5 = '1'
        val_6 = '2'
        val_7 = 'b'
        ordered_list = OrderedStringList(asc=False)
        ordered_list.add(val_1)
        ordered_list.add(val_2)
        ordered_list.add(val_3)
        ordered_list.add(val_4)
        ordered_list.add(val_5)
        ordered_list.add(val_6)
        ordered_list.add(val_7)
        self.assertEqual(val_7, ordered_list.get_all()[0].value)
        self.assertEqual(val_3, ordered_list.get_all()[1].value)
        self.assertEqual(val_2, ordered_list.get_all()[2].value)
        self.assertEqual(val_6, ordered_list.get_all()[3].value)
        self.assertEqual(val_5, ordered_list.get_all()[4].value)
        self.assertEqual(val_4, ordered_list.get_all()[5].value)
        self.assertEqual(val_1, ordered_list.get_all()[6].value)
        self.assertEqual(val_1, ordered_list.find(val_1).value)
        self.assertEqual(val_2, ordered_list.find(val_2).value)
        self.assertEqual(val_3, ordered_list.find(val_3).value)
        self.assertEqual(val_4, ordered_list.find(val_4).value)
        self.assertEqual(val_5, ordered_list.find(val_5).value)
        self.assertEqual(val_6, ordered_list.find(val_6).value)
        self.assertEqual(val_7, ordered_list.find(val_7).value)
        self.assertEqual(None, ordered_list.find('15'))

    # deleting block
    def test_delete_from_empty(self):
        ordered_list = OrderedList(asc=True)
        self.assertEqual(ordered_list.head, None)
        self.assertEqual(ordered_list.tail, None)
        self.assertEqual(ordered_list.get_all(), [])
        ordered_list.delete(15)
        self.assertEqual(ordered_list.head, None)
        self.assertEqual(ordered_list.tail, None)
        self.assertEqual(ordered_list.get_all(), [])

    def test_delete_none(self):
        val_1 = 12
        val_2 = 55
        val_3 = 100
        ordered_list = OrderedList(asc=True)
        self.assertEqual(ordered_list.head, None)
        self.assertEqual(ordered_list.tail, None)
        self.assertEqual(ordered_list.get_all(), [])
        ordered_list.delete(None)
        self.assertEqual(ordered_list.head, None)
        self.assertEqual(ordered_list.tail, None)
        self.assertEqual(ordered_list.get_all(), [])
        ordered_list.delete(1000)
        self.assertEqual(ordered_list.head, None)
        self.assertEqual(ordered_list.tail, None)
        self.assertEqual(ordered_list.get_all(), [])

    def test_delete_head(self):
        val_1 = 12
        val_2 = 55
        val_3 = 100
        ordered_list = OrderedList(asc=True)
        ordered_list.add(val_1)
        ordered_list.add(val_2)
        ordered_list.add(val_3)
        ordered_list.delete(12)
        self.assertEqual(ordered_list.head.value, val_2)
        self.assertEqual(ordered_list.tail.value, val_3)
        self.assertEqual(ordered_list.get_all()[0].value, val_2)
        self.assertEqual(ordered_list.get_all()[1].value, val_3)
        self.assertEqual(ordered_list.len(), 2)
        ordered_list = OrderedList(asc=False)
        ordered_list.add(val_1)
        ordered_list.add(val_2)
        ordered_list.add(val_3)
        ordered_list.delete(12)
        self.assertEqual(ordered_list.head.value, val_3)
        self.assertEqual(ordered_list.tail.value, val_2)
        self.assertEqual(ordered_list.get_all()[0].value, val_3)
        self.assertEqual(ordered_list.get_all()[1].value, val_2)
        self.assertEqual(ordered_list.len(), 2)
        val_1 = ' a'
        val_2 = ' с '
        val_3 = 'b '
        ordered_list = OrderedStringList(asc=True)
        ordered_list.add(val_1)
        ordered_list.add(val_2)
        ordered_list.add(val_3)
        ordered_list.delete(' a')
        self.assertEqual(ordered_list.head.value, val_3)
        self.assertEqual(ordered_list.tail.value, val_2)
        self.assertEqual(ordered_list.get_all()[0].value, val_3)
        self.assertEqual(ordered_list.get_all()[1].value, val_2)
        self.assertEqual(ordered_list.len(), 2)
        ordered_list = OrderedStringList(asc=False)
        ordered_list.add(val_1)
        ordered_list.add(val_2)
        ordered_list.add(val_3)
        ordered_list.delete(' a')
        self.assertEqual(ordered_list.head.value, val_2)
        self.assertEqual(ordered_list.tail.value, val_3)
        self.assertEqual(ordered_list.get_all()[0].value, val_2)
        self.assertEqual(ordered_list.get_all()[1].value, val_3)
        self.assertEqual(ordered_list.len(), 2)

    def test_delete_tail(self):
        val_1 = 12
        val_2 = 55
        val_3 = 100
        ordered_list = OrderedList(asc=True)
        ordered_list.add(val_1)
        ordered_list.add(val_2)
        ordered_list.add(val_3)
        ordered_list.delete(100)
        self.assertEqual(ordered_list.head.value, val_1)
        self.assertEqual(ordered_list.tail.value, val_2)
        self.assertEqual(ordered_list.get_all()[0].value, val_1)
        self.assertEqual(ordered_list.get_all()[1].value, val_2)
        self.assertEqual(ordered_list.len(), 2)
        ordered_list = OrderedList(asc=False)
        ordered_list.add(val_1)
        ordered_list.add(val_2)
        ordered_list.add(val_3)
        ordered_list.delete(100)
        self.assertEqual(ordered_list.head.value, val_2)
        self.assertEqual(ordered_list.tail.value, val_1)
        self.assertEqual(ordered_list.get_all()[0].value, val_2)
        self.assertEqual(ordered_list.get_all()[1].value, val_1)
        self.assertEqual(ordered_list.len(), 2)
        val_1 = ' a'
        val_2 = ' с '
        val_3 = 'b '
        ordered_list = OrderedStringList(asc=True)
        ordered_list.add(val_1)
        ordered_list.add(val_2)
        ordered_list.add(val_3)
        ordered_list.delete(val_2)
        self.assertEqual(ordered_list.head.value, val_1)
        self.assertEqual(ordered_list.tail.value, val_3)
        self.assertEqual(ordered_list.get_all()[0].value, val_1)
        self.assertEqual(ordered_list.get_all()[1].value, val_3)
        self.assertEqual(ordered_list.len(), 2)
        ordered_list = OrderedStringList(asc=False)
        ordered_list.add(val_1)
        ordered_list.add(val_2)
        ordered_list.add(val_3)
        ordered_list.delete(val_2)
        self.assertEqual(ordered_list.head.value, val_3)
        self.assertEqual(ordered_list.tail.value, val_1)
        self.assertEqual(ordered_list.get_all()[0].value, val_3)
        self.assertEqual(ordered_list.get_all()[1].value, val_1)
        self.assertEqual(ordered_list.len(), 2)

    # cleaning block
    def test_clean(self):
        val_1 = 12
        val_2 = 55
        val_3 = 100
        ordered_list = OrderedList(asc=True)
        ordered_list.add(val_1)
        ordered_list.add(val_2)
        ordered_list.add(val_3)
        ordered_list.clean(asc=True)
        self.assertEqual(ordered_list.len(), 0)
        self.assertEqual(ordered_list.head, None)
        self.assertEqual(ordered_list.tail, None)
        ordered_list.add(val_1)
        ordered_list.add(val_2)
        ordered_list.add(val_3)
        ordered_list.clean(asc=False)
        self.assertEqual(ordered_list.len(), 0)
        self.assertEqual(ordered_list.head, None)
        self.assertEqual(ordered_list.tail, None)

    def test_clean_string(self):
        val_1 = 'a'
        val_2 = 'b'
        val_3 = 'c'
        ordered_list = OrderedStringList(asc=True)
        ordered_list.add(val_1)
        ordered_list.add(val_2)
        ordered_list.add(val_3)
        ordered_list.clean(asc=True)
        self.assertEqual(ordered_list.len(), 0)
        self.assertEqual(ordered_list.head, None)
        self.assertEqual(ordered_list.tail, None)
        ordered_list.add(val_1)
        ordered_list.add(val_2)
        ordered_list.add(val_3)
        ordered_list.clean(asc=False)
        self.assertEqual(ordered_list.len(), 0)
        self.assertEqual(ordered_list.head, None)
        self.assertEqual(ordered_list.tail, None)

    # manipulating with empty
    def check_empty(self):
        ordered_list = OrderedList(asc=True)
        self.assertEqual(ordered_list.len(), 0)
        self.assertEqual(ordered_list.find(100), None)
        ordered_list.delete(100)
        self.assertEqual(ordered_list.len(), 0)
        self.assertEqual(ordered_list.find(100), None)
        self.assertEqual(ordered_list.head, None)
        self.assertEqual(ordered_list.tail, None)

if __name__ == '__main__':
    unittest.main()
