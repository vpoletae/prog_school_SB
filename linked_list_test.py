import unittest
import random
from Linked_list import Node, LinkedList

n1 = Node(15)
n2 = Node(16)
n3 = Node(17)
n1.next = n2
n2.next = n3
linked_list = LinkedList()
linked_list.add_in_tail(n1)
linked_list.add_in_tail(n2)
linked_list.add_in_tail(n3)
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
        unlinked_list = self.obj.convert_to_unlinked_list()
        random_index = random.randint(0, (len(unlinked_list)-1))
        random_number = unlinked_list[random_index]
        counter = int()
        for i in unlinked_list:
            if i == random_number:
                counter += 1
            else:
                pass
        self.assertTrue(self.obj.find_all(random_number))
        self.assertTrue(isinstance(self.obj.find_all(random_number), list))
        self.assertEqual(len(self.obj.find_all(random_number)), counter)

    def test_delete(self):
        unlinked_list_before = self.obj.convert_to_unlinked_list()
        random_index = random.randint(0, (len(unlinked_list_before)-1))
        self.obj.delete(int(unlinked_list_before[random_index]))
        unlinked_list_after = self.obj.convert_to_unlinked_list()
        self.assertNotEqual(unlinked_list_before, unlinked_list_after)

    # def test_clean(self):
    #     self.assertFalse(self.obj.clean())
    #     self.assertEqual(self.obj.clean(), None)

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
