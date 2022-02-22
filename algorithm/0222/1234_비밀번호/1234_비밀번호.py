import sys
sys.stdin = open('input.txt')

def isEmpty(stack):
    if not stack:
        True
    else:
        False

def after_skip(string):
    stack = []
    for char in string:
        if not stack:
            stack.append(char)
        elif stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return "".join(stack)

for tc in range(1, 11):
    n, string = input().split()
    result = after_skip(string)
    print(f'#{tc} {result}')
