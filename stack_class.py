class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return "Stack Underflow"
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# Example usage
s = Stack()
s.push(5)
s.push(15)
s.push(25)

print("Top of stack:", s.peek())
print("Popped:", s.pop())
print("Is empty?", s.is_empty())
print("Size:", s.size())
