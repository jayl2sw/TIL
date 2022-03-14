import sys

sys.stdin = open('input.txt')


def my_sort(n, array):
    for i in range(n-1):
        min_v = min(array[i+1:])
        idx = array[i+1:].index(min_v)+i+1
        if array[i] > min_v:
            array[i], array[idx] = array[idx], array[i]

    return array


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int,input().split()))
    print(f'#{tc} {" ".join(map(str, my_sort(n, arr)))}')


