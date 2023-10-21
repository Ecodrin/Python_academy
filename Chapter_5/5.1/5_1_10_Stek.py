class Stack:
    def __init__(self):
        self.que = []

    def push(self, item):
        self.que.append(item)

    def pop(self):
        return self.que.pop(-1)

    def is_empty(self):
        return len(self.que) == 0


stack = Stack()
for item in range(10):
    stack.push(item)
while not stack.is_empty():
    print(stack.pop(), end=" ")