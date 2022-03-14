import sys

sys.stdin = open('input.txt')


def max(set):
    max_val = -int(1e9)
    for i in set:
        if max_val < i:
            max_val = i
    return max_val


def min(set) :
    min_val = int(1e9)
    for i in set:
        if min_val > i:
            min_val = i
    return min_val


def dump(n, array):
    for _ in range(n):
        max_idx = array.index(max(array))
        min_idx = array.index(min(array))

        if max_idx - min_idx <= 1:
            return 0

        array[max_idx] -= 1
        array[min_idx] += 1

    return max(array) - min(array)


for tc in range(1, 11):
    n = int(input())
    array = list(map(int,input().split()))
    print(f'#{tc} {dump(n, array)}')