import sys
sys.stdin = open('input.txt')


def check_bracket(string):
    array = []
    for char in string:
        if char == '(':
            array.append('(')
        elif char == ')':
            if array:
                array.pop()
            else:
                return -1

    if not array:
        return 1
    else:
        return -1


T = int(input())
for tc in range(1, T+1):
    string = sys.stdin.readline()
    result = check_bracket(string)
    print(f'#{tc} {result}')