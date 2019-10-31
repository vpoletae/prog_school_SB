import unittest
from Linked_list2 import Node, LinkedList2

class Test_Linked_list(unittest.TestCase):

    def test_find_absence(self):
        n1 = Node(12)
        n2 = Node(55)
        n1.next = n2
        n2.prev = n1
        linked_list = LinkedList2()
        linked_list.add_in_tail(n1)
        linked_list.add_in_tail(n2)
        val = 100 # non-existing value
        self.assertEqual(None, linked_list.find(val))

    def test_find_empty(self):
        linked_list = LinkedList2()
        val = 100
        self.assertEqual(None, linked_list.find(val))

    def test_find_first(self):
        n1 = Node(12)
        n2 = Node(55)
        n3 = Node(13)
        n4 = Node(55)
        n1.next = n2
        n2.prev = n1
        n2.next = n3
        n3.prev = n2
        n3.next = n4
        n4.prev = n3
        linked_list = LinkedList2()
        linked_list.add_in_tail(n1)
        linked_list.add_in_tail(n2)
        linked_list.add_in_tail(n3)
        linked_list.add_in_tail(n4)
        val = 55 # want to find
        prev_value = 12 # to compare with prev
        next_value = 13 # to compare with after
        found = linked_list.find(val)
        self.assertEqual(val, found.value)
        self.assertEqual(prev_value, found.prev.value)
        self.assertEqual(next_value, found.next.value)

    def test_find_all_absence(self):
        n1 = Node(12)
        n2 = Node(55)
        n3 = Node(13)
        n4 = Node(55)
        n1.next = n2
        n2.prev = n1
        n2.next = n3
        n3.prev = n2
        n3.next = n4
        n4.prev = n3
        linked_list = LinkedList2()
        linked_list.add_in_tail(n1)
        linked_list.add_in_tail(n2)
        linked_list.add_in_tail(n3)
        linked_list.add_in_tail(n4)
        val = 100 # want to find
        self.assertEqual([], linked_list.find_all(val))

    def test_find_all_empty(self):
        linked_list = LinkedList2()
        val = 100
        self.assertEqual([], linked_list.find_all(val))

    def test_find_all(self):
        n1 = Node(12)
        n2 = Node(55)
        n3 = Node(13)
        n4 = Node(55)
        n5 = Node(100)
        n1.next = n2
        n2.prev = n1
        n2.next = n3
        n3.prev = n2
        n3.next = n4
        n4.prev = n3
        n4.next = n5
        n5.prev = n4
        linked_list = LinkedList2()
        linked_list.add_in_tail(n1)
        linked_list.add_in_tail(n2)
        linked_list.add_in_tail(n3)
        linked_list.add_in_tail(n4)
        linked_list.add_in_tail(n5)
        val = 55 # want to find
        len_match = 2 # len of found list
        found = linked_list.find_all(val)
        self.assertEqual(len_match, len(found))
        self.assertEqual(n1.value, found[0].prev.value)
        self.assertEqual(n3.value, found[0].next.value)
        self.assertEqual(n3.value, found[1].prev.value)
        self.assertEqual(n5.value, found[1].next.value)

    def test_del_non_existing(self):
        n1 = Node(12)
        n2 = Node(55)
        n3 = Node(13)
        n4 = Node(55)
        n5 = Node(100)
        n1.next = n2
        n2.prev = n1
        n2.next = n3
        n3.prev = n2
        n3.next = n4
        n4.prev = n3
        n4.next = n5
        n5.prev = n4
        linked_list = LinkedList2()
        linked_list.add_in_tail(n1)
        linked_list.add_in_tail(n2)
        linked_list.add_in_tail(n3)
        linked_list.add_in_tail(n4)
        linked_list.add_in_tail(n5)
        val = 1000 # want to find
        linked_list.delete(val, all=False)
        self.assertEqual(n1.value, linked_list.head.value)
        self.assertEqual(n5.value, linked_list.tail.value)
        self.assertEqual(n4.value,
                        linked_list.tail.prev.value)

    def test_del_from_empty(self):
        linked_list = LinkedList2()
        val = 100
        before = linked_list
        linked_list.delete(val)
        self.assertEqual(before, linked_list)

    def test_delete_false_list1_head(self):
        n1 = Node(12)
        n1.next = None
        n1.prev = None
        linked_list = LinkedList2()
        linked_list.add_in_tail(n1)
        val = 12
        linked_list.delete(val, all=False)
        self.assertEqual(None, linked_list.head)
        self.assertEqual(None, linked_list.tail)
        self.assertEqual(None, linked_list.find(val))

    def test_delete_false_list_head(self):
        n1 = Node(12)
        n2 = Node(55)
        n3 = Node(13)
        n4 = Node(55)
        n5 = Node(100)
        n1.next = n2
        n2.prev = n1
        n2.next = n3
        n3.prev = n2
        n3.next = n4
        n4.prev = n3
        n4.next = n5
        n5.prev = n4
        linked_list = LinkedList2()
        linked_list.add_in_tail(n1)
        linked_list.add_in_tail(n2)
        linked_list.add_in_tail(n3)
        linked_list.add_in_tail(n4)
        linked_list.add_in_tail(n5)
        val = 12 # want to find
        linked_list.delete(val)
        self.assertEqual(n2.value, linked_list.head.value)
        self.assertEqual(n2.prev, None)
        self.assertEqual(n5.value, linked_list.tail.value)
        self.assertEqual(n4.value, linked_list.tail.prev.value)

    def test_delete_false_list_tail(self):
        n1 = Node(12)
        n2 = Node(55)
        n3 = Node(13)
        n4 = Node(55)
        n5 = Node(100)
        n1.next = n2
        n2.prev = n1
        n2.next = n3
        n3.prev = n2
        n3.next = n4
        n4.prev = n3
        n4.next = n5
        n5.prev = n4
        linked_list = LinkedList2()
        linked_list.add_in_tail(n1)
        linked_list.add_in_tail(n2)
        linked_list.add_in_tail(n3)
        linked_list.add_in_tail(n4)
        linked_list.add_in_tail(n5)
        val = 100 # want to find
        linked_list.delete(val)
        self.assertEqual(n1.value, linked_list.head.value)
        self.assertEqual(n4.value, linked_list.tail.value)
        self.assertEqual(n3.value,
                        linked_list.tail.prev.value)
        self.assertEqual(n5.prev, None)

    def test_delete_false_list_mid(self):
        n1 = Node(12)
        n2 = Node(55)
        n3 = Node(13)
        n4 = Node(55)
        n5 = Node(100)
        n1.next = n2
        n2.prev = n1
        n2.next = n3
        n3.prev = n2
        n3.next = n4
        n4.prev = n3
        n4.next = n5
        n5.prev = n4
        linked_list = LinkedList2()
        linked_list.add_in_tail(n1)
        linked_list.add_in_tail(n2)
        linked_list.add_in_tail(n3)
        linked_list.add_in_tail(n4)
        linked_list.add_in_tail(n5)
        val = 13 # want to find
        linked_list.delete(val)
        self.assertEqual(n1.value, linked_list.head.value)
        self.assertEqual(n5.value, linked_list.tail.value)
        self.assertEqual(n2.next.value, n4.value)
        self.assertEqual(n4.prev.value, n2.value)
        self.assertEqual(None, linked_list.find(val))

    def test_del_all_true_non_existing(self):
        n1 = Node(12)
        n2 = Node(55)
        n3 = Node(13)
        n4 = Node(55)
        n5 = Node(100)
        n1.next = n2
        n2.prev = n1
        n2.next = n3
        n3.prev = n2
        n3.next = n4
        n4.prev = n3
        n4.next = n5
        n5.prev = n4
        linked_list = LinkedList2()
        linked_list.add_in_tail(n1)
        linked_list.add_in_tail(n2)
        linked_list.add_in_tail(n3)
        linked_list.add_in_tail(n4)
        linked_list.add_in_tail(n5)
        val = 1000 # want to find
        linked_list.delete(val, all=True)
        self.assertEqual(n1.value, linked_list.head.value)
        self.assertEqual(n5.value, linked_list.tail.value)
        self.assertEqual(n4.value,
                        linked_list.tail.prev.value)

    def test_del_all_true_from_empty(self):
        linked_list = LinkedList2()
        val = 100
        before = linked_list
        linked_list.delete(val)
        self.assertEqual(before, linked_list)

    def test_del_all_true_list1_head(self):
        n1 = Node(12)
        n1.next = None
        n1.prev = None
        linked_list = LinkedList2()
        linked_list.add_in_tail(n1)
        val = 12
        linked_list.delete(val, all=True)
        self.assertEqual(None, linked_list.head)
        self.assertEqual(None, linked_list.tail)
        self.assertEqual(None, linked_list.find(val))

    def test_del_all_true_list_head(self):
        n1 = Node(12)
        n2 = Node(55)
        n3 = Node(13)
        n4 = Node(12)
        n5 = Node(100)
        n1.next = n2
        n2.prev = n1
        n2.next = n3
        n3.prev = n2
        n3.next = n4
        n4.prev = n3
        n4.next = n5
        n5.prev = n4
        linked_list = LinkedList2()
        linked_list.add_in_tail(n1)
        linked_list.add_in_tail(n2)
        linked_list.add_in_tail(n3)
        linked_list.add_in_tail(n4)
        linked_list.add_in_tail(n5)
        val = 12 # want to find
        linked_list.delete(val, all=True)
        self.assertEqual(n2.value, linked_list.head.value)
        self.assertEqual(n2.prev, None)
        self.assertEqual(n5.value, linked_list.tail.value)
        self.assertEqual(n3.value, linked_list.tail.prev.value)
        self.assertEqual(n3.next.value, linked_list.tail.value)
        self.assertEqual(None, linked_list.find(val))

    def test_delete_true_list_tail(self):
        n1 = Node(12)
        n2 = Node(55)
        n3 = Node(100)
        n4 = Node(13)
        n5 = Node(100)
        n1.next = n2
        n2.prev = n1
        n2.next = n3
        n3.prev = n2
        n3.next = n4
        n4.prev = n3
        n4.next = n5
        n5.prev = n4
        linked_list = LinkedList2()
        linked_list.add_in_tail(n1)
        linked_list.add_in_tail(n2)
        linked_list.add_in_tail(n3)
        linked_list.add_in_tail(n4)
        linked_list.add_in_tail(n5)
        val = 100 # want to find
        linked_list.delete(val, all=True)
        self.assertEqual(n1.value, linked_list.head.value)
        self.assertEqual(n4.value, linked_list.tail.value)
        self.assertEqual(n2.value,
                        linked_list.tail.prev.value)
        self.assertEqual(n2.next.value,
                        linked_list.tail.value)
        self.assertEqual(None, linked_list.find(val))

    def test_delete_true_list_mid(self):
        n1 = Node(12)
        n2 = Node(55)
        n3 = Node(55)
        n4 = Node(55)
        n5 = Node(100)
        n1.next = n2
        n2.prev = n1
        n2.next = n3
        n3.prev = n2
        n3.next = n4
        n4.prev = n3
        n4.next = n5
        n5.prev = n4
        linked_list = LinkedList2()
        linked_list.add_in_tail(n1)
        linked_list.add_in_tail(n2)
        linked_list.add_in_tail(n3)
        linked_list.add_in_tail(n4)
        linked_list.add_in_tail(n5)
        val = 55 # want to find
        linked_list.delete(val, all=True)
        self.assertEqual(n1.value, linked_list.head.value)
        self.assertEqual(n5.value, linked_list.tail.value)
        self.assertEqual(n1.next.value, linked_list.tail.value)
        self.assertEqual(linked_list.tail.prev.value, n1.value)
        self.assertEqual(None, linked_list.find(val))

    def test_delete_true_all_all(self):
        n1 = Node(55)
        n2 = Node(55)
        n3 = Node(55)
        n4 = Node(55)
        n5 = Node(55)
        n1.next = n2
        n2.prev = n1
        n2.next = n3
        n3.prev = n2
        n3.next = n4
        n4.prev = n3
        n4.next = n5
        n5.prev = n4
        linked_list = LinkedList2()
        linked_list.add_in_tail(n1)
        linked_list.add_in_tail(n2)
        linked_list.add_in_tail(n3)
        linked_list.add_in_tail(n4)
        linked_list.add_in_tail(n5)
        val = 55 # want to find
        linked_list.delete(val, all=True)
        self.assertEqual(None, linked_list.head)
        self.assertEqual(None, linked_list.tail)
        self.assertEqual(None, linked_list.find(val))

    def test_delete_true_all_except_first(self):
        n1 = Node(10)
        n2 = Node(55)
        n3 = Node(55)
        n4 = Node(55)
        n5 = Node(55)
        n1.next = n2
        n2.prev = n1
        n2.next = n3
        n3.prev = n2
        n3.next = n4
        n4.prev = n3
        n4.next = n5
        n5.prev = n4
        linked_list = LinkedList2()
        linked_list.add_in_tail(n1)
        linked_list.add_in_tail(n2)
        linked_list.add_in_tail(n3)
        linked_list.add_in_tail(n4)
        linked_list.add_in_tail(n5)
        val = 55 # want to find
        linked_list.delete(val, all=True)
        self.assertEqual(n1.value, linked_list.head.value)
        self.assertEqual(n1.value, linked_list.tail.value)
        self.assertEqual(None, linked_list.find(val))

    def test_delete_true_all_except_last(self):
        n1 = Node(55)
        n2 = Node(55)
        n3 = Node(55)
        n4 = Node(55)
        n5 = Node(10)
        n1.next = n2
        n2.prev = n1
        n2.next = n3
        n3.prev = n2
        n3.next = n4
        n4.prev = n3
        n4.next = n5
        n5.prev = n4
        linked_list = LinkedList2()
        linked_list.add_in_tail(n1)
        linked_list.add_in_tail(n2)
        linked_list.add_in_tail(n3)
        linked_list.add_in_tail(n4)
        linked_list.add_in_tail(n5)
        val = 55 # want to find
        linked_list.delete(val, all=True)
        self.assertEqual(n5.value, linked_list.head.value)
        self.assertEqual(n5.value, linked_list.tail.value)
        self.assertEqual(None, linked_list.find(val))

    def test_clean(self):
        n1 = Node(55)
        n2 = Node(53)
        n3 = Node(12)
        n4 = Node(0)
        n5 = Node(10)
        n1.next = n2
        n2.prev = n1
        n2.next = n3
        n3.prev = n2
        n3.next = n4
        n4.prev = n3
        n4.next = n5
        n5.prev = n4
        linked_list = LinkedList2()
        linked_list.add_in_tail(n1)
        linked_list.add_in_tail(n2)
        linked_list.add_in_tail(n3)
        linked_list.add_in_tail(n4)
        linked_list.add_in_tail(n5)
        linked_list.clean()
        self.assertEqual(linked_list.head, None)
        self.assertEqual(linked_list.tail, None)
        self.assertEqual(linked_list.len(), 0)
        self.assertEqual(linked_list.find(n1.value), None)
        self.assertEqual(linked_list.find(n2.value), None)
        self.assertEqual(linked_list.find(n3.value), None)
        self.assertEqual(linked_list.find(n4.value), None)
        self.assertEqual(linked_list.find(n5.value), None)

    def test_len_empty(self):
        linked_list = LinkedList2()
        self.assertEqual(0, linked_list.len())

    def test_len_one(self):
        n1 = Node(55)
        n1.next = None
        n1.prev = None
        linked_list = LinkedList2()
        linked_list.add_in_tail(n1)
        self.assertEqual(1, linked_list.len())

    def test_len(self):
        n1 = Node(55)
        n2 = Node(53)
        n3 = Node(12)
        n4 = Node(0)
        n5 = Node(10)
        n1.next = n2
        n2.prev = n1
        n2.next = n3
        n3.prev = n2
        n3.next = n4
        n4.prev = n3
        n4.next = n5
        n5.prev = n4
        linked_list = LinkedList2()
        linked_list.add_in_tail(n1)
        linked_list.add_in_tail(n2)
        linked_list.add_in_tail(n3)
        linked_list.add_in_tail(n4)
        linked_list.add_in_tail(n5)
        self.assertEqual(5, linked_list.len())

    def test_insert_no_new(self):
        n1 = Node(12)
        n2 = Node(55)
        n3 = Node(55)
        n4 = Node(55)
        n5 = Node(100)
        n1.next = n2
        n2.prev = n1
        n2.next = n3
        n3.prev = n2
        n3.next = n4
        n4.prev = n3
        n4.next = n5
        n5.prev = n4
        linked_list = LinkedList2()
        linked_list.add_in_tail(n1)
        linked_list.add_in_tail(n2)
        linked_list.add_in_tail(n3)
        linked_list.add_in_tail(n4)
        linked_list.add_in_tail(n5)
        before = linked_list
        linked_list.insert(n1, None)
        self.assertEqual(before, linked_list)
        self.assertEqual(before.len(), linked_list.len())

    def test_insert_no_after_empty(self):
        linked_list = LinkedList2()
        node_to_add = Node(15)
        new_len = 1
        linked_list.insert(None, node_to_add)
        self.assertEqual(node_to_add.value,
                        linked_list.head.value)
        self.assertEqual(node_to_add.value,
                        linked_list.tail.value)
        self.assertEqual(node_to_add.prev, None)
        self.assertEqual(node_to_add.next, None)
        self.assertEqual(linked_list.len(), new_len)
        self.assertEqual(linked_list.find(15), node_to_add)

    def test_insert_no_after_full(self):
        n1 = Node(12)
        n2 = Node(55)
        n3 = Node(55)
        n4 = Node(55)
        n5 = Node(100)
        n1.next = n2
        n2.prev = n1
        n2.next = n3
        n3.prev = n2
        n3.next = n4
        n4.prev = n3
        n4.next = n5
        n5.prev = n4
        linked_list = LinkedList2()
        linked_list.add_in_tail(n1)
        linked_list.add_in_tail(n2)
        linked_list.add_in_tail(n3)
        linked_list.add_in_tail(n4)
        linked_list.add_in_tail(n5)
        node_to_add = Node(15)
        new_len = 6
        linked_list.insert(None, node_to_add)
        self.assertEqual(node_to_add.value,
                        linked_list.tail.value)
        self.assertEqual(n1.value, linked_list.head.value)
        self.assertEqual(node_to_add.prev, n5)
        self.assertEqual(node_to_add.next, None)
        self.assertEqual(linked_list.len(), new_len)
        self.assertEqual(linked_list.find(15), node_to_add)

    def test_insert(self):
        n1 = Node(12)
        n2 = Node(55)
        n3 = Node(55)
        n4 = Node(55)
        n5 = Node(100)
        n1.next = n2
        n2.prev = n1
        n2.next = n3
        n3.prev = n2
        n3.next = n4
        n4.prev = n3
        n4.next = n5
        n5.prev = n4
        linked_list = LinkedList2()
        linked_list.add_in_tail(n1)
        linked_list.add_in_tail(n2)
        linked_list.add_in_tail(n3)
        linked_list.add_in_tail(n4)
        linked_list.add_in_tail(n5)
        node_to_add = Node(15)
        new_len = 6
        linked_list.insert(n2, node_to_add)
        self.assertEqual(node_to_add.prev, n2)
        self.assertEqual(node_to_add.next, n3)
        self.assertEqual(n3.prev, node_to_add)
        self.assertEqual(n2.next, node_to_add)
        self.assertEqual(n1, linked_list.head)
        self.assertEqual(n5, linked_list.tail)
        self.assertEqual(linked_list.len(), new_len)
        self.assertEqual(linked_list.find(15), node_to_add)

    def test_add_in_head_empty(self):
        linked_list = LinkedList2()
        node_to_add = Node(15)
        new_len = 1
        linked_list.add_in_head(node_to_add)
        self.assertEqual(node_to_add.value,
                        linked_list.head.value)
        self.assertEqual(node_to_add.value,
                        linked_list.tail.value)
        self.assertEqual(node_to_add.prev, None)
        self.assertEqual(node_to_add.next, None)
        self.assertEqual(linked_list.len(), new_len)
        self.assertEqual(linked_list.find(15), node_to_add)

    def test_add_in_head_full(self):
        n1 = Node(12)
        n2 = Node(55)
        n3 = Node(55)
        n4 = Node(55)
        n5 = Node(100)
        n1.next = n2
        n2.prev = n1
        n2.next = n3
        n3.prev = n2
        n3.next = n4
        n4.prev = n3
        n4.next = n5
        n5.prev = n4
        linked_list = LinkedList2()
        linked_list.add_in_tail(n1)
        linked_list.add_in_tail(n2)
        linked_list.add_in_tail(n3)
        linked_list.add_in_tail(n4)
        linked_list.add_in_tail(n5)
        node_to_add = Node(15)
        new_len = 6
        linked_list.add_in_head(node_to_add)
        self.assertEqual(node_to_add.value,
                        linked_list.head.value)
        self.assertEqual(n1.prev.value, node_to_add.value)
        self.assertEqual(node_to_add.prev, None)
        self.assertEqual(node_to_add.next, n1)
        self.assertEqual(linked_list.len(), new_len)
        self.assertEqual(linked_list.find(15), node_to_add)

if __name__ == '__main__':
    unittest.main()
