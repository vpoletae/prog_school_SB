class Heap:

    def __init__(self):
        self.HeapArray = [] # хранит неотрицательные числа-ключи

    def MakeHeap(self, a, depth):
	    # создаём массив кучи HeapArray из заданного
        # размер массива выбираем на основе глубины depth
        assert 2 ** (depth + 1) - 1 >= len(a)
        heap_size = 0
        for i in range(depth+1):
            heap_size += (2 ** i)
        self.HeapArray = [None] * heap_size
        for i in a:
            self.Add(i)


        # def MakeHeap(self, a, depth):
    	#     # создаём массив кучи HeapArray из заданного
        #     # размер массива выбираем на основе глубины depth
        #     assert 2 ** (depth + 1) - 1 >= len(a)
        #     heap_size = 0
        #     for i in range(depth+1):
        #         heap_size += (2 ** i)
        #     self.HeapArray = [None] * heap_size
        #     if len(self.HeapArray) >= len(a):
        #         sorted_array = sorted(a, reverse=True)
        #         for i in range(len(a)):
        #             self.HeapArray[i] = sorted_array[i]

    def GetMax(self):
        # вернуть значение корня и перестроить кучу
        if not self.HeapArray:
	        return -1 # если куча пуста

        root = self.HeapArray[0]
        if len(self.HeapArray) == 1:
            self.HeapArray[0] = None
        else:
            last = self.HeapArray[1] # assign last to second elem
            if last is None:
                self.HeapArray[0] = None
            else:
                for i in range(1, len(self.HeapArray)+1):
                    if self.HeapArray[-i] is not None:
                        last = self.HeapArray[-i]
                        self.HeapArray[-i] = None
                        break
                self.HeapArray[0] = last
                self.reorder_heap_up_down(self.HeapArray, last)
        return root

    def reorder_heap_up_down(self, array, value, index=0):
        left_index = 2 * index + 1
        right_index = 2 * index + 2
        if left_index > len(array)-1:
            pass
        else:
            left_child_val = array[left_index]
            right_child_val = array[right_index]
            if left_child_val is None:
                pass
            else:
                if right_child_val is None:
                    if value < left_child_val:
                        array[index] = left_child_val
                        array[left_index] = value
                        index = left_index
                else:
                    if left_child_val > right_child_val:
                        if value < left_child_val:
                            array[index] = left_child_val
                            array[left_index] = value
                            index = left_index
                    else:
                        if value < right_child_val:
                            array[index] = right_child_val
                            array[right_index] = value
                            index = right_index
                    self.reorder_heap_up_down(array, value, index)

    def Add(self, key):
	    # добавляем новый элемент key в кучу и перестраиваем её
        if self.HeapArray[0] is None:
            self.HeapArray[0] = key
            return True
        if self.HeapArray[-1] is not None:
            return False # если куча вся заполнена
        else:
            i = -1
            while self.HeapArray[i] is None:
                i -= 1
            index_to_add =  len(self.HeapArray) + i + 1
            self.HeapArray[index_to_add] = key
            self.reorder_heap_down_up(self.HeapArray, key, child_index=index_to_add) #add params
            return True

    def reorder_heap_down_up(self, array, key, child_index):
        # определить, это левый или правый потомок
        # Определить индекс родителя
        # Сравнить значения потомка и родителя
        # Если потомок >, поменять местами
        if child_index == 0:
            pass
        else:
            if child_index % 2 == 0: #правый потомок
                parent_index = int((child_index - 2) / 2) # right_child = parent * 2 + 2
            else:
                parent_index = int((child_index - 1) / 2)

            if key > array[parent_index]:
                parent_val = array[parent_index]
                array[parent_index] = key
                array[child_index] = parent_val
                child_index = parent_index
                self.reorder_heap_down_up(array, key, child_index)
            else:
                pass
