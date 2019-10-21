import unittest
import random
from Linked_list import Node, LinkedList

n1 = Node(15)
n2 = Node(16)
n3 = Node(17)
n4 = Node(16)
n1.next = n2
n2.next = n3
linked_list = LinkedList()
linked_list.add_in_tail(n1)
linked_list.add_in_tail(n2)
linked_list.add_in_tail(n3)
linked_list.add_in_tail(n4)
test_obj = linked_list

class Test_Linked_list(unittest.TestCase):
    def setUp(self):
        self.obj = test_obj

    def test_find(self):
        unlinked_list = self.obj.convert_to_unlinked_list()
        random_index = random.randint(0, (len(unlinked_list)-1))
        random_number = unlinked_list[random_index]
        self.assertTrue(self.obj.find(random_number))
        self.assertEqual(self.obj.find(random_number).value, random_number)

    def test_find_all(self):
        to_find = 16
        to_be_found = [n2, n4]
        unlinked_list = self.obj.convert_to_unlinked_list()
        random_index = random.randint(0, (len(unlinked_list)-1))
        random_number = unlinked_list[random_index]
        counter = int()
        for i in unlinked_list:
            if i == random_number:
                counter += 1
            else:
                pass
        self.assertTrue(self.obj.find_all(to_find), to_be_found)
        self.assertTrue(self.obj.find_all(random_number))
        self.assertTrue(isinstance(self.obj.find_all(random_number), list))
        self.assertEqual(len(self.obj.find_all(random_number)), counter)

    def test_delete(self):
        unlinked_list_before = self.obj.convert_to_unlinked_list()
        random_index = random.randint(0, (len(unlinked_list_before)-1))
        self.obj.delete(int(unlinked_list_before[random_index]))
        unlinked_list_after = self.obj.convert_to_unlinked_list()
        self.assertNotEqual(unlinked_list_before, unlinked_list_after)

    def test_delete_first(self):
        n1 = Node(15)
        n2 = Node(16)
        n3 = Node(17)
        n4 = Node(16)
        n1.next = n2
        n2.next = n3
        n3.next = n4
        linked_list = LinkedList()
        linked_list.add_in_tail(n1)
        linked_list.add_in_tail(n2)
        linked_list.add_in_tail(n3)
        linked_list.add_in_tail(n4)
        linked_list.delete(n1.value)
        self.assertNotIn(n1.value, linked_list.convert_to_unlinked_list())
        self.assertEqual(n2, linked_list.head)

    def test_delete_last(self):
        n1 = Node(16)
        n2 = Node(16)
        n3 = Node(17)
        n4 = Node(15)
        n1.next = n2
        n2.next = n3
        n3.next = n4
        linked_list = LinkedList()
        linked_list.add_in_tail(n1)
        linked_list.add_in_tail(n2)
        linked_list.add_in_tail(n3)
        linked_list.add_in_tail(n4)
        linked_list.delete(n4.value)
        self.assertNotIn(n4.value, linked_list.convert_to_unlinked_list())
        self.assertEqual(n3, linked_list.tail)

    def test_delete_none(self):
        n1 = Node(16)
        n2 = Node(16)
        n3 = Node(17)
        n4 = Node(15)
        node_none_value = 1000
        n1.next = n2
        n2.next = n3
        n3.next = n4
        linked_list = LinkedList()
        linked_list.add_in_tail(n1)
        linked_list.add_in_tail(n2)
        linked_list.add_in_tail(n3)
        linked_list.add_in_tail(n4)
        linked_list.delete(node_none_value)
        self.assertEqual(n1, linked_list.head)
        self.assertEqual(n4, linked_list.tail)

    def test_delete_one(self):
        n1 = Node(15)
        linked_list = LinkedList()
        linked_list.add_in_tail(n1)
        len_before = linked_list.len()
        linked_list.delete(n1.value)
        len_after = linked_list.len()
        self.assertEqual(1, len_before)
        self.assertEqual(0, len_after)
        self.assertEqual(None, linked_list.head)
        self.assertEqual(None, linked_list.tail)

    def test_delete_one_of_two(self):
        n1 = Node(15)
        n2 = Node(17)
        n1.next = n2
        linked_list = LinkedList()
        linked_list.add_in_tail(n1)
        linked_list.add_in_tail(n2)
        linked_list.delete(n2.value)
        len_after = linked_list.len()
        self.assertEqual(1, len_after)
        self.assertEqual(n1, linked_list.head)
        self.assertEqual(n1, linked_list.tail)

    def test_delete_first_and_last(self):
        n1 = Node(15)
        n2 = Node(16)
        n3 = Node(17)
        n4 = Node(15)
        n1.next = n2
        n2.next = n3
        n3.next = n4
        linked_list = LinkedList()
        linked_list.add_in_tail(n1)
        linked_list.add_in_tail(n2)
        linked_list.add_in_tail(n3)
        linked_list.add_in_tail(n4)
        len_before = linked_list.len()
        linked_list.delete(n1.value, True)
        len_after = linked_list.len()
        self.assertEqual(4, len_after+2)
        self.assertEqual(n2, linked_list.head)
        self.assertEqual(n3, linked_list.tail)

    def test_delete_all_equal(self):
        n1 = Node(15)
        n2 = Node(15)
        n3 = Node(15)
        n4 = Node(15)
        n1.next = n2
        n2.next = n3
        n3.next = n4
        linked_list = LinkedList()
        linked_list.add_in_tail(n1)
        linked_list.add_in_tail(n2)
        linked_list.add_in_tail(n3)
        linked_list.add_in_tail(n4)
        linked_list.delete(n1.value, True)
        len_after = linked_list.len()
        self.assertEqual(0, len_after)
        self.assertEqual(None, linked_list.head)
        self.assertEqual(None, linked_list.tail)

    def test_clean(self):
        n1 = Node(15)
        n2 = Node(16)
        n3 = Node(17)
        n4 = Node(15)
        n1.next = n2
        n2.next = n3
        n3.next = n4
        linked_list = LinkedList()
        linked_list.add_in_tail(n1)
        linked_list.add_in_tail(n2)
        linked_list.add_in_tail(n3)
        linked_list.add_in_tail(n4)
        linked_list.clean()
        self.assertEqual(linked_list.head, None)
        self.assertEqual(linked_list.tail, None)
        self.assertEqual(linked_list.len(), 0)


    def test_len(self):
        self.assertTrue(self.obj.len())
        unlinked_list = self.obj.convert_to_unlinked_list()
        self.assertEqual(self.obj.len(), len(unlinked_list))

    def test_insert(self):
        unlinked_list_before = self.obj.convert_to_unlinked_list()
        random_index = random.randint(0, (len(unlinked_list_before)-1))
        after_node = unlinked_list_before[random_index]
        new_node = random.randrange(1, 100)
        test_obj.insert(after_node, new_node)
        unlinked_list_after = self.obj.convert_to_unlinked_list()
        self.assertNotEqual(unlinked_list_before, unlinked_list_after)
        self.assertIn(new_node, unlinked_list_after)

if __name__ == '__main__':
    unittest.main()
