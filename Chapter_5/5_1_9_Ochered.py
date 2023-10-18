class Queue:
    def __init__(self):
        self.que = []

    def push(self, item):
        self.que.append(item)

    def pop(self):
        return self.que.pop(0)

    def is_empty(self):
        return len(self.que) == 0


queue = Queue()
for item in range(10):
    queue.push(item)
while not queue.is_empty():
    print(queue.pop(), end=" ")
