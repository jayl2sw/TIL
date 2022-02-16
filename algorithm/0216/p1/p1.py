import sys
from collections import deque

sys.stdin = open('input.txt')


def reverse1(string):
    print(string[::-1])


def reverse2(string):
    temp = deque()
    for s in string:
        temp.appendleft(s)
    print(''.join(temp))


def reverse3(string):
    for i in range(len(string)-1, -1, -1):
        print(string[i], end='')
    print()


def reverse4(string):
    result = ''
    for char in string:
        result = char + result
    print(result)


T = int(input())
for tc in range(1,5):
    s = input()
    print(f'#{tc}', end=' ')
    exec(f'reverse{tc}(s)')

