import sys
sys.stdin = open('input.txt')

def change_to_postfix(string):
    operator = ['+', '-', '*', '/']
    stack = []
    result = ''
    for char in string:
        if char not in operator:
            result += char
        else:
            stack.append(char)

    for i in range(len(stack)):
        result += stack.pop()

    return result


T = int(input())
for tc in range(1, T+1):
    string = input()
    print(f'#{tc} {change_to_postfix(string)}')