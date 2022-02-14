import sys

sys.stdin = open("input.txt")


def max_sum(array):
    result = 0
    for i in range(100):
        result = max(result, sum(array[i]))
    for i in range(100):
        sub_total = 0
        for j in range(100):
            sub_total += array[j][i]
        result = max(sub_total, result)

    result = max(result, sum([array[i][i] for i in range(100)]))
    result = max(result, sum([array[i][99 - i] for i in range(100)]))
    return result


for tc in range(1, 11):
    n = int(input())
    array = [list(map(int, input().split())) for _ in range(100)]
    print(f'#{n} {max_sum(array)}')
