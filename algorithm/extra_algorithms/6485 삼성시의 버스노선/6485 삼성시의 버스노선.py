import sys

sys.stdin = open('input.txt')

def change(start, end, array):
    for i in range(start, end+1):
        array[i] += 1

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    array = [0] * 5001
    for _ in range(n):
        a, b = map(int,input().split())
        change(a, b, array)
    p = int(input())
    print(f'#{tc}', end=' ')
    for _ in range(p):
        print(array[int(input())], end=' ')
    print()