class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) == 0:
            return None
        else:
            first_elem = self.queue[0]
            self.queue = self.queue[1:]
            return first_elem

    def size(self):
        return len(self.queue)
