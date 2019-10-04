class Node:
    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        node = self.head
        matched_list = []
        while node is not None:
            if node.value == val:
                matched_list.append(node.value)
            node = node.next
        # print(matched_list)
        return matched_list

    def delete(self, val, all=False):
        node = self.head
        previous_node = None
        if all == False:
            if val == node.value:
                self.head = node.next
            else:
                while node != None:
                    if node.value == val:
                        node = node.next
                        break
                    previous_node = node
                    node = node.next
                previous_node.next = node
        elif all == True:
            if val == node.value:
                self.head = node.next
            else:
                previous_node = node
                node = node.next
            while node != None:
                if node.value == val:
                    node = node.next
                    previous_node.next = node
                else:
                    previous_node = node
                    node = node.next
        else:
            pass

    def clean(self):
        node = self.head
        previous_node = None
        while node != None:
            previous_node = node
            node = node.next
            previous_node.next = None
        self.head = None

    def len(self):
        node = self.head
        counter = int()
        while node != None:
            counter += 1
            node = node.next
        return counter

    def insert(self, afterNode, newNode):
        node = self.head
        if afterNode and newNode:
            if newNode != None:
                newNode = Node(newNode)
                if afterNode != None:
                    afterNode = self.find(afterNode)
                    next_afterNode = afterNode.next
                    afterNode.next = newNode
                    newNode.next = next_afterNode
                else:
                    newNode = self.head
                    newNode.next = node
            else:
                pass
        else:
            pass

n1 = Node(12)
n2 = Node(55)
n3 = Node(55)
s_list = LinkedList()
s_list.add_in_tail(n1)
s_list.add_in_tail(n2)
s_list.add_in_tail(n3)
s_list.add_in_tail(Node(128))
# s_list.print_all_nodes()
# s_list.find_all(55)
# s_list.delete(55, all=True)
# s_list.clean()
# length = s_list.len()
# print(length)
s_list.insert(128, 1000)
s_list.print_all_nodes()
