import sys

sys.stdin = open('input.txt')


def my_sort(n, array):
    for i in range(n-1):
        min_v = int(1e9)
        for j in range(i+1, n):
            if array[j] < min_v:
                min_v = array[j]
                min_idx = j
        if array[i] > array[min_idx]:
            array[i], array[min_idx] = array[min_idx], array[i]

    return array


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int,input().split()))
    print(f'#{tc} {" ".join(map(str, my_sort(n, arr)))}')


