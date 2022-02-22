import sys
sys.stdin = open('input.txt')

def isEmpty(stack):
    if not stack:
        True
    else:
        False

def len_after_skip(string):
    stack = []
    for char in string:
        if isEmpty(stack):
            stack.append(char)
        elif stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return len(stack)



T = int(input())
for tc in range(1, T+1):
    string = input()
    print(f'#{tc} {len_after_skip(string)}')