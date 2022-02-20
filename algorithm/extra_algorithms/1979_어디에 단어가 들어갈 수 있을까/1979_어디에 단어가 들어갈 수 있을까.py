import sys
from copy import deepcopy

sys.stdin = open('input.txt')


def check_horizontal(n, k, arr):
    array = deepcopy(arr)
    count = 0
    minus = 0
    for i in range(n):
        for j in range(1, n):
            if array[i][j] == 1:
                array[i][j] += array[i][j - 1]
            if array[i][j] == k:
                count += 1
            if array[i][j] == k + 1:
                minus += 1
    result = count - minus
    if result < 0:
        result = 0
    return result


def check_vertical(n, k, arr):
    array = deepcopy(arr)
    count = 0
    minus = 0
    for i in range(n):
        for j in range(1, n):
            if array[j][i] == 1:
                array[j][i] += array[j][i - 1]
            if array[j][i] == k:
                count += 1
            if array[j][i] == k + 1:
                minus += 1
    result = count - minus
    if result < 0:
        result = 0
    return result


T = int(input())
for tc in range(1, T + 1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    print(check_vertical(n, k, arr) + check_horizontal(n, k, arr))
