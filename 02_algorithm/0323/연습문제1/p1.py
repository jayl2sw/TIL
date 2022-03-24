import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    arr = input()

    while arr:
        now = arr[:7]
        arr = arr[7:]
        result = 0
        for i in range(7):
            result = result * 2 + int(now[i])
        print(result, end=' ')
    print()