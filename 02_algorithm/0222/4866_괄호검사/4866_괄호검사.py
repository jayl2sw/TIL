import sys
sys.stdin = open('input.txt')

def check_bracket(string):
    stack = []
    for bracket in string:
        if bracket == '(':
            stack.append('(')
        elif bracket == '{':
            stack.append('{')
        elif bracket == ')':
            if not stack:
                return 0
            if stack[-1] == '(':
                stack.pop()
            else:
                return 0
        elif bracket == '}':
            if not stack:
                return 0
            if stack[-1] == '{':
                stack.pop()
            else:
                return 0
    if not stack:
        return 1
    else:
        return 0

T = int(input())
for tc in range(1, T+1):
    string = input()
    print(f'#{tc} {check_bracket(string)}')