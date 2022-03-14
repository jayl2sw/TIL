import sys

sys.stdin = open('input.txt')

def max(*args):
    max_val = -int(1e9)
    for i in args:
        if max_val < i:
            max_val = i
    return max_val

def check_view(array, N):
    total = 0
    for i in range(2, N - 2):
        around_max = max(array[i - 2], array[i - 1], array[i + 2], array[i + 1])
        if array[i] > around_max:
            total += (array[i] - around_max)

    return total


for tc in range(1, 11):
    N = int(input())
    array = list(map(int, input().split()))
    print(f'#{tc} {check_view(array, N)}')
