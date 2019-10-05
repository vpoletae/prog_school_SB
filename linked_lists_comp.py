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

n1 = Node(15)
n2 = Node(16)
n3 = Node(17)
n1.next = n2
n2.next = n3

linked_list_1 = LinkedList()
linked_list_1.add_in_tail(n1)
linked_list_1.add_in_tail(n2)
linked_list_1.add_in_tail(n3)

n4 = Node(-15)
n5 = Node(-16)
n6 = Node(-17)
n4.next = n5
n5.next = n6

linked_list_2= LinkedList()
linked_list_2.add_in_tail(n4)
linked_list_2.add_in_tail(n5)
linked_list_2.add_in_tail(n6)

result_list = linked_list_compare(linked_list_1, linked_list_2)
print(result_list)
