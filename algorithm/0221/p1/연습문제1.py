class Stack:
    def __init__(self, size):
        self.arr = [None] * size
        self.size = size
        self.top = -1

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
            print('Stack overflow')
        else:
            self.top += 1
            self.arr[self.top] = n

    def pop(self):
        if self.isEmpty():
            raise 'Stack underflow'
        else:
            result = self.arr[self.top]
            self.arr[self.top] = None
            self.top -= 1
            return result

    def peek(self):
        if self.isEmpty():
            raise 'There is not any element'
        else:
            result = self.arr[self.top]
            return result

    def clear(self):
        self.arr = [None] * self.size

    def size(self):
        len(self.arr)

    def __len__(self):
        return len(self.arr) - self.arr.count(None)

    def __str__(self):
        return str(self.arr[:self.top+1:1])


st = Stack(5)

st.push('A')
st.push('B')
st.push('C')
print(st)
print(len(st))
print(st.pop())
print(st.pop())
print(st.pop())