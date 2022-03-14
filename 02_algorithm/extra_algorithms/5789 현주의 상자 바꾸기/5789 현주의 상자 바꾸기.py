import sys

sys.stdin = open('input.txt')

def change(start, end, array, number):
    for i in range(start-1, end):
        array[i] = number

T = int(input())
for tc in range(1, T+1):
    n, q = map(int, input().split())
    array = [0] * n
    for i in range(1, q+1):
        start, end = map(int, input().split())
        change(start, end, array, i)
    print(f'#{tc} {" ".join(map(str,array))}')




