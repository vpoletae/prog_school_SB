from Linked_list import Node, LinkedList

def linked_list_compare(obj_1, obj_2):
    if obj_1.len_() == obj_2.len_():
        obj_1_list = []
        node = obj_1.head
        while node is not None:
            obj_1_list.append(node.value)
            node = node.next

        obj_2_list = []
        node = obj_2.head
        while node is not None:
            obj_2_list.append(node.value)
            node = node.next

        result_list = [(x + y) for (x, y) in zip(obj_1_list, obj_2_list)]
        return result_list
    else:
        return None
