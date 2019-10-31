class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

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
        prev_node = None
        if all == False:
            while node != None:
                if node.value == val:
                    if node == self.head:
                        if node.next == None:
                            node = None
                            self.head = None
                            self.tail = None
                            break
                        else:
                            self.head = node.next
                            node = node.next
                            node.prev = None
                            break
                    elif node == self.tail:
                        self.tail = node.prev
                        node.prev.next = None
                        node.prev = None
                        break
                    else:
                        prev_node = node.prev
                        node = node.next
                        prev_node.next = node
                        node.prev = prev_node
                        break
                node = node.next
        elif all == True:
            while node != None:
                if node.value == val:
                    if node == self.head:
                        if node.next == None:
                            node = None
                            self.head = None
                            self.tail = None
                            break
                        else:
                            self.head = node.next
                            node = node.next
                            node.prev = None
                    elif node == self.tail:
                        self.tail = node.prev
                        node.prev.next = None
                        node.prev = None
                        break
                    else:
                        prev_node = node.prev
                        node = node.next
                        prev_node.next = node
                        node.prev = prev_node
                else:
                    node = node.next
        else:
            return None

    def clean(self):
        node = self.head
        prev_node = None
        while node != None:
            if node.next == None:
                node.prev = None
                node = None
            else:
                prev_node = node
                node = node.next
                prev_node.next = None
                node.prev = prev_node
        self.head = None
        self.tail = None

    def len(self):
        node = self.head
        counter = int()
        while node != None:
            counter += 1
            node = node.next
        return counter

    def insert(self, afterNode, newNode):
        node = self.head
        if newNode:
            if afterNode:
                after_Node = self.find(afterNode.value)
                if after_Node:
                    if after_Node == self.tail:
                        after_Node.next = newNode
                        self.tail = newNode
                        newNode.prev = after_Node
                    else:
                        next_afterNode = after_Node.next
                        after_Node.next = newNode
                        newNode.prev = after_Node
                        newNode.next = next_afterNode
                        next_afterNode.prev = newNode
                else:
                    self.tail.next = newNode
                    newNode.prev = self.tail
                    self.tail = newNode
            else:
                if self.head == None:
                    self.head = newNode
                    self.tail = newNode
                    newNode.next = None
                    newNode.prev = None
                else:
                    self.tail.next = newNode
                    newNode.prev = self.tail
                    self.tail = newNode
        else:
            pass

    def add_in_head(self, newNode):
        if self.head == None:
            self.head = newNode
            self.tail = newNode
            newNode.next = None
            newNode.prev = None
        else:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
