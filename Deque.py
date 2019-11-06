class Deque:
    def __init__(self):
        self.deque = []

    def addFront(self, item):
        self.deque.insert(0, item)

    def addTail(self, item):
        self.deque.append(item)

    def removeFront(self):
        if len(self.deque) == 0:
            return None
        else:
            last_elem = self.deque.pop()
            return last_elem

    def removeTail(self):
        if len(self.deque) == 0:
            return None
        else:
            first_elem = self.deque[0]
            del self.deque[0]
            return first_elem

    def size(self):
        return len(self.deque)
