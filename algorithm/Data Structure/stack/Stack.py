# stack data structure

class Stack:

    # stack이 최초 생성될 때 필요한 정보들
    # stack의 크기를 기본 값으로 받아와야한다.
    def __init__(self, size):
        self.size = size
        # stack을 저장할 자료구조
        # 최초 stack 생성 시, 각 위치에는 값이 없다.
        self.arr = [None] * size
        # stack의 최상단
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

    def push(self, char):
        if self.isFull:
            print("이미 꽉 찼습니다.")
        else:
            self.top += 1
            self.arr[self.top] = char

    def pop(self):
        if not self.is_empty():
            result = self.arr[self.top]
            self.arr[self.top] = None
            self.top -= 1
            return result


s1 = Stack(5)
print(s1.arr)
print(s1.size)
print(s1.top)
print("=" * 30)

print(s1.isEmpty())
