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
                matched_list.append(node)
            node = node.next
        return matched_list

    def delete(self, val, all=False):
        node = self.head
        previous_node = None
        if all == False:
            while node != None:
                if node.value == val:
                    if node == self.head:
                        self.head = node.next
                        break
                    elif node == self.tail:
                        self.tail = previous_node
                        break
                    else:
                        node = node.next
                        previous_node.next = node
                        break
                previous_node = node
                node = node.next
        elif all == True:
            while node != None:
                if node == self.head:
                    if node.value == val:
                        self.head = node.next
                    previous_node = node
                    node = node.next
                elif node == self.tail:
                    if node.value == val:
                        self.tail = previous_node
                        previous_node.next = None
                        break
                    node = node.next
                else:
                    if node.value == val:
                        previous_node.next = node.next
                        node = node.next
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
                    if afterNode == self.tail:
                        afterNode.next = newNode
                        self.tail = newNode
                    else:
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

    def convert_to_unlinked_list(self):
        node = self.head
        simple_list = []
        while node != None:
            simple_list.append(node.value)
            node = node.next
        return simple_list
