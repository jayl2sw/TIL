import sys
sys.stdin = open('input.txt')

def operate(a, b, operator):
    if operator == '+':
        return a+b
    elif operator == '-':
        return a-b
    elif operator == '*':
        return a*b
    elif operator == '/':
        return a//b

def calculate_Forth(array):
    operator = ['+', '-', '*', '/']
    stack = []
    for char in array:
        if char == '.':
            break
        elif char not in operator:
            stack.append(int(char))
        elif char in operator:
            if len(stack) < 2:
                return 'error'
            a = stack.pop()
            b = stack.pop()
            temp = operate(b, a, char)
            stack.append(temp)
        else:
            return 'error'
    if len(stack) == 1:
        return stack[0]
    else:
        return 'error'

T = int(input())
for tc in range(1, T+1):
    array = list(input().split())
    result = calculate_Forth(array)
    print(f'#{tc} {result}')
