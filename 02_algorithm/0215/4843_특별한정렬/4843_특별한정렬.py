import sys

sys.stdin = open('input.txt')


def wierd_sort(array):
    array.sort()
    result = []
    for i in range(5):
        result.append(array[-i-1])
        result.append(array[i])
    print(' '.join(map(str,result)))


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    array = list(map(int, input().split()))
    print(f'#{tc}', end=' ')
    wierd_sort(array)

