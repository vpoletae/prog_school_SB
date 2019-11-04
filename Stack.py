class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if len(self.stack) == 0:
            return None
        else:
            last_elem = self.stack.pop()
            return last_elem

    def push(self, value):
        self.stack.append(value)

    def peek(self):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1]
