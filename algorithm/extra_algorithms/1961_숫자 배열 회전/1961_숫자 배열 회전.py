import sys
sys.stdin = open('input.txt')


def rotation(n, array):
    for i in range(n):
        for j in range(n):
            print(array[n-j-1][i], end='')
        print(' ', end='')

        for k in range(n):
            print(array[n-i-1][n-k-1], end='')
        print(' ', end='')
        for g in range(n):
            print(array[g][n-i-1], end='')
        print()


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    array = [list(map(int,input().split()))for _ in range(n)]
    print(f'#{tc}')
    rotation(n, array)