import sys

sys.stdin = open("input.txt")


def abs_sum(array, x, y):
    result = 0
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5:
            result += abs(array[x][y] - array[nx][ny])

    return result


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    array = [list(map(int, input().split())) for _ in range(n)]
    result = 0
    for i in range(5):
        for j in range(5):
            result += abs_sum(array, i, j)
    print(f'{tc} {result}')