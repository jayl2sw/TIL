import sys

sys.stdin = open('input.txt')


def dump(n, array):
    for i in range(n):
        max_col = array.index(max(array))
        min_col = array.index(min(array))

        array[max_col] -= 1
        array[min_col] += 1

    return max(array) - min(array)


for tc in range(1, 11):
    n = int(input())
    array = list(map(int,input().split()))
    print(f'#{tc} {dump(n, array)}')