class aBST:

    def __init__(self, depth):
        # правильно рассчитайте размер массива для дерева глубины depth:
        tree_size = depth + 1
        self.Tree = [None] * tree_size # массив ключей

    def FindKeyIndex(self, key):
        # ищем в массиве индекс ключа
        # начинаем с корня
        # до тех пор пока индекс меньше размера дерева:
        #     если дерево[индекс]:
        #         если ключ == дерево[индекс]: # значение узла с заданным индексом
        #             вернуть индекс
        #         если ключ > дерево[индекс]:
        #             индекс = 2 * индекс + 2
        #         иначе:
        #             индекс = 2 * индекс + 1
        #     иначе:
        #         вернуть -(индекс)
        # вернуть None
        node_index = 0
        while node_index <= len(self.Tree):
            node_value = self.Tree[node_index]
            if node_value:
                if key == node_value:
                    return node_index
                elif key > node_value:
                    node_index = 2 * node_index + 2
                else:
                    node_index = 2 * node_index + 1
            else:
                if node_index == 0:
                    return 0
                else:
                    return -(node_index)
        return None # не найден

    def AddKey(self, key):
        # добавляем ключ в массив
        index = self.FindKeyIndex(key)
        if index is not None:
            if index <= 0:
                self.Tree[-(index)] = key
                return -(index)
            else:
                return index
        else:
            return -1
        # индекс добавленного/существующего ключа или -1 если не удалось
