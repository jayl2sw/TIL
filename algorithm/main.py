import sys; sys.stdin = open('input.txt')
class Stack:
    def __init__(self, size):
        self.size = size
        self.arr = [None] * size
        self.top = -1

    def push(self, n):
        self.top += 1
        self.arr[self.top] = n

    def pop(self):
        if not self.is_empty():
            result = self.arr[self.top]
            self.arr[self.top] = None
            self.top -= 1
            return result

    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False



# for tc in range(1, 2):
#     n = int(input())
#     lst = list(input())
#     stack = Stack(n)
#     result = []
#     opr_rank = {'*' : 2, '/' : 2, '-' : 1, '+' : 1}
#
#     post = []
#     for i in lst:
#         if i in opr_rank:
#             #연산자는 스택이 비었으면 push한다
#             if stack.arr[0] == None:
#                 stack.push(i)
#
#             else:
#                 #i가 연산자인데 스택이 비어있지 않으면서
#                 #스택 맨위 연산자의 우선순위가 i보다 같거나 크다면
#                 #stack의 연산자를 pop한뒤 출력하고
#                 #현재 i는 스택에 push
#                 while opr_rank.get(stack.arr[stack.top]) >= opr_rank.get(i):
#                     result += stack.pop()
#                     if stack.is_empty():
#                         break
#                 stack.push(i)
#
#                 #스택 맨위의 연산자 우선순위가 i보다 낮다면
#                 #i를 push
#         #연산자가 아니면
#         #숫자이면
#         else:
#             result += i
#
#     while not stack.is_empty():
#         result += stack.pop()
def post_cal(arr):
    stack = [] * len(arr)

    for i in arr:
        # 연산자에 해당하면
        if i in ('+', '-', '/', '*'):
            try:
                b = stack.pop()
                a = stack.pop()
                if i == '+':
                    c = int(a) + int(b)
                elif i == '-':
                    c = int(a) - int(b)
                elif i == '/':
                    c = int(a) // int(b)
                elif i == '*':
                    c = int(a) * int(b)
                stack.append(c)
            # 연산자가 나왔는데도 연달아 pop할 원소가 없다는 것은
            # 에러라는 뜻
            except:
                # 한번 에러가 발생하면 다음걸 볼 필요 없음
                break
        else:
            stack.append(int(i))
    return stack

for tc in range(1,11):
    n = int(input())
    lst = list(input())
    stack = Stack(n)

    opr_rank = {'*' : 2, '/' : 2, '-' : 1, '+' : 1}

    post = []
    for i in lst:
        if i in opr_rank:
            #연산자는 스택이 비었으면 push한다
            if stack.arr[0] == None:
                stack.push(i)

            else:
                #i가 연산자인데 스택이 비어있지 않으면서
                #스택 맨위 연산자의 우선순위가 i보다 같거나 크다면
                #stack의 연산자를 pop한뒤 출력하고
                #현재 i는 스택에 push
                while opr_rank.get(stack.arr[stack.top]) >= opr_rank.get(i):
                    post += stack.pop()
                    if stack.is_empty():
                        break
                stack.push(i)
        #숫자이면
        else:
            post += i

    for i in range(n):
        if stack.arr[i] != None:
            post += stack.pop()

    print(post_cal(post))


