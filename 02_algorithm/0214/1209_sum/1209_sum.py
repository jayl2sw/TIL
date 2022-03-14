import sys

sys.stdin = open("input.txt")


def max(*args):
    max_v = 0
    for i in args:
        if max_v < i:
            max_v = i
    return max_v


def sum(array):
    total = 0
    for i in array:
        total += i
    return total


def max_sum(array):
    result = 0
    for i in range(100):
        result = max(result, sum(array[i]))  # 행 합 확인
    for i in range(100):
        sub_total = 0
        for j in range(100):
            sub_total += array[j][i]         # 열 합 확인
        result = max(sub_total, result)

    result = max(result, sum([array[i][i] for i in range(100)])) # 대각선 합 확인
    result = max(result, sum([array[i][99 - i] for i in range(100)]))
    return result


for tc in range(1, 11):
    n = int(input())
    array = [list(map(int, input().split())) for _ in range(100)]
    print(f'#{n} {max_sum(array)}')
