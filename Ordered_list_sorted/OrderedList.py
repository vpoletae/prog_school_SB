class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        result = int()
        if v1.value < v2.value:
            result = -1
        elif v1.value == v2.value:
            result = 0
        else:
            result = 1
        return result

    def add(self, val):
        node = self.head
        prev_node = None
        new_node = Node(val)

        if node is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = None
            new_node.prev = None
        else:
            while node != None:
                if self.__ascending:
                    if self.compare(node, new_node) == 1:
                        break
                else:
                    if self.compare(node, new_node) == -1:
                        break
                prev_node = node
                node = node.next

            if node == None:
                prev_node.next = new_node
                new_node.prev = prev_node
                self.tail = new_node
            else:
                if self.__ascending:
                    if node == self.head:
                        self.head = new_node
                        new_node.next = node
                        node.prev = new_node
                    else:
                        prev_node.next = new_node
                        new_node.prev = prev_node
                        new_node.next = node
                        node.prev = new_node
                else:
                    if node == self.head:
                        self.head = new_node
                        new_node.next = node
                        node.prev = new_node
                    else:
                        prev_node.next = new_node
                        new_node.prev = prev_node
                        new_node.next = node
                        node.prev = new_node


    def find(self, val):
        node = self.head
        find_node = Node(val)
        while node != None:
            if self.compare(node, find_node) == 0:
                return node
            else:
                if self.__ascending:
                    if self.compare(node, find_node) == 1:
                        return None
                    else:
                        node = node.next
                else:
                    if self.compare(node, find_node) == -1:
                        return None
                    else:
                        node = node.next
        return None

    def delete(self, val):
        node = self.head
        prev_node = None
        next_node = None
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
                    next_node = node.next
                    node.prev = None
                    node.next = None
                    prev_node.next = next_node
                    next_node.prev = prev_node
                    break
            else:
                prev_node = node
                node = node.next

    def clean(self, asc):
        self.__ascending = asc
        if self.__ascending:
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
        else:
            node = self.tail
            next_node = None
            while node != None:
                if node.prev == None:
                    node.prev = None
                    node = None
                else:
                    next_node = node
                    node = node.prev
                    next_node.prev = None
                    node.next = next_node
            self.head = None
            self.tail = None

    def len(self):
        node = self.head
        counter = int()
        while node != None:
            counter += 1
            node = node.next
        return counter

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r

class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        result = int()
        v1_text = v1.value.strip(' \t\n\r')
        v2_text = v2.value.strip(' \t\n\r')
        if v1_text < v2_text:
            result = -1
        elif v1_text == v2_text:
            if v1.value < v2.value:
                result = -1
            elif v1.value == v2.value:
                result = 0
            else:
                result = 1
        else:
            result = 1
        return result
