import unittest
from dyn_array import DynArray

class Test_Linked_list(unittest.TestCase):

    def test_insert_out_of_range_before(self):
        da = DynArray()
        for i in range(1, 11):
            da.append(i)
        prev_count = da.count
        prev_capacity = da.capacity
        raised = False
        try:
            da.insert(-1, 1000)
        except:
            raised = True
        self.assertEqual(raised, True)
        self.assertEqual(prev_count, da.count)
        self.assertEqual(prev_capacity, da.capacity)

    def test_insert_out_of_range_after(self):
        da = DynArray()
        for i in range(1, 11):
            da.append(i)
        prev_count = da.count
        prev_capacity = da.capacity
        raised = False
        try:
            da.insert(100, 1000)
        except:
            raised = True
        self.assertEqual(raised, True)
        self.assertEqual(prev_count, da.count)
        self.assertEqual(prev_capacity, da.capacity)

    def test_insert_last_cap_in(self):
        da = DynArray()
        for i in range(10):
            da.append(i)
        prev_count = da.count
        prev_capacity = da.capacity
        da.insert(9, 1000)
        self.assertEqual(da[9], 1000)
        self.assertEqual(da[8], 8)
        self.assertEqual(da[10], 9)
        self.assertEqual(prev_count+1, da.count)
        self.assertEqual(prev_capacity, da.capacity)

    def test_insert_last_cap_out(self):
        da = DynArray()
        for i in range(1, 17):
            da.append(i)
        prev_count = da.count
        prev_capacity = da.capacity
        da.insert(15, 1000)
        self.assertEqual(da[15], 1000)
        self.assertEqual(da[16], 16)
        self.assertEqual(da[14], 15)
        self.assertEqual(prev_count+1, da.count)
        self.assertEqual(prev_capacity*2, da.capacity)

    def test_insert_cap_in(self):
        da = DynArray()
        for i in range(10):
            da.append(i)
        prev_count = da.count
        prev_capacity = da.capacity
        da.insert(0, 1000)
        self.assertEqual(da[0], 1000)
        self.assertEqual(da[1], 0)
        self.assertEqual(da[10], 9)
        self.assertEqual(prev_count+1, da.count)
        self.assertEqual(prev_capacity, da.capacity)

    def test_insert_cap_out(self):
        da = DynArray()
        for i in range(16):
            da.append(i)
        prev_count = da.count
        prev_capacity = da.capacity
        da.insert(0, 1000)
        self.assertEqual(da[0], 1000)
        self.assertEqual(da[1], 0)
        self.assertEqual(da[16], 15)
        self.assertEqual(prev_count+1, da.count)
        self.assertEqual(prev_capacity*2, da.capacity)

    def test_delete_out_of_range_before(self):
        da = DynArray()
        for i in range(1, 11):
            da.append(i)
        prev_count = da.count
        prev_capacity = da.capacity
        raised = False
        try:
            da.delete(-1, 1000)
        except:
            raised = True
        self.assertEqual(raised, True)
        self.assertEqual(prev_count, da.count)
        self.assertEqual(prev_capacity, da.capacity)

    def test_delete_out_of_range_after(self):
        da = DynArray()
        for i in range(1, 11):
            da.append(i)
        prev_count = da.count
        prev_capacity = da.capacity
        raised = False
        try:
            da.delete(100, 1000)
        except:
            raised = True
        self.assertEqual(raised, True)
        self.assertEqual(prev_count, da.count)
        self.assertEqual(prev_capacity, da.capacity)

    def test_delete_last_cap_in_no_resize(self):
        da = DynArray()
        for i in range(10):
            da.append(i)
        prev_count = da.count
        prev_capacity = da.capacity
        da.delete(9)
        raised = False
        try:
            da[9]
        except:
            raised = True
        self.assertEqual(raised, True)
        self.assertEqual(prev_count, da.count+1)
        self.assertEqual(prev_capacity, da.capacity)

    def test_delete_last_cap_in_is_resize_threshold(self):
        da = DynArray()
        for i in range(17):
            da.append(i)
        prev_count = da.count
        prev_capacity = da.capacity
        da.delete(16)
        raised = False
        try:
            da[16]
        except:
            raised = True
        self.assertEqual(raised, True)
        self.assertEqual(prev_count, da.count+1)
        self.assertEqual(prev_capacity, da.capacity)

    def test_delete_last_cap_in_is_resize(self):
        da = DynArray()
        for i in range(17):
            da.append(i)
        prev_count = da.count
        prev_capacity = da.capacity
        da.delete(16)
        da.delete(15)
        raised = False
        try:
            da[15]
        except:
            raised = True
        self.assertEqual(raised, True)
        self.assertEqual(prev_count, da.count+2)
        self.assertEqual(int(prev_capacity/1.5), da.capacity)

    def test_delete_last_cap_out(self):
        da = DynArray()
        for i in range(17):
            da.append(i)
        da.capacity = 1000
        prev_count = da.count
        prev_capacity = da.capacity
        da.delete(16)
        raised = False
        try:
            da[16]
        except:
            raised = True
        self.assertEqual(raised, True)
        self.assertEqual(prev_count, da.count+1)
        self.assertEqual(int(prev_capacity/1.5), da.capacity)

    def test_delete_first_cap_in(self):
        da = DynArray()
        for i in range(10):
            da.append(i)
        prev_count = da.count
        prev_capacity = da.capacity
        da.delete(0)
        raised = False
        try:
            da[9]
        except:
            raised = True
        self.assertEqual(da[0], 1)
        self.assertEqual(da[8], 9)
        self.assertEqual(raised, True)
        self.assertEqual(prev_count, da.count+1)
        self.assertEqual(prev_capacity, da.capacity)

    def test_delete_random_cap_in(self):
        da = DynArray()
        for i in range(10):
            da.append(i)
        prev_count = da.count
        prev_capacity = da.capacity
        da.delete(5)
        raised = False
        try:
            da[9]
        except:
            raised = True
        self.assertEqual(da[4], 4)
        self.assertEqual(da[5], 6)
        self.assertEqual(da[8], 9)
        self.assertEqual(raised, True)
        self.assertEqual(prev_count, da.count+1)
        self.assertEqual(prev_capacity, da.capacity)

    def test_delete_cap_out(self):
        da = DynArray()
        for i in range(17):
            da.append(i)
        prev_count = da.count
        prev_capacity = da.capacity
        da.delete(0)
        da.delete(10)
        raised = False
        try:
            da[15]
        except:
            raised = True
        self.assertEqual(da[0], 1)
        self.assertEqual(da[10], 12)
        self.assertEqual(da[9], 10)
        self.assertEqual(da[11], 13)
        self.assertEqual(raised, True)
        self.assertEqual(prev_count, da.count+2)
        self.assertEqual(int(prev_capacity/1.5), da.capacity)

    def test_delete_from_empty(self):
        da = DynArray()
        prev_count = da.count
        prev_capacity = da.capacity
        raised = False
        try:
            da.delete(0)
        except:
            raised = True
        self.assertEqual(raised, True)
        self.assertEqual(prev_count, da.count)
        self.assertEqual(prev_capacity, da.capacity)

if __name__ == '__main__':
    unittest.main()
