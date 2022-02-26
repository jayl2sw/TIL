class Queue:
    def __init__(self, size):
        self.arr = []
        self.top = -1
        self.size = size

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def isFull(self):
        if self.top == self.size - 1:
            return True
        else:
            return False

    def push(self, n):
        if self.isFull():
            raise OverflowError
        else:
            self.arr += [n]
            self.top += 1

    def pop(self):
        if self.isEmpty():
            raise IndexError
        else:
            temp = self.arr[0]
            del self.arr[0]
            self.top -= 1
            return temp

    def peek(self):
        return self.arr[self.top]

    def __len__(self):
        return len(self.arr)

    def __str__(self):
        return ", ".join(map(str, self.arr))

q = Queue(4)

q.push(1)
q.push(2)
q.push(3)
print(q)

print(q.pop())
print(q.pop())
print(q.pop())