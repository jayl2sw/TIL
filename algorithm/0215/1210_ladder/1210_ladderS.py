import sys
sys.stdin = open('input.txt')


def find_destination(array):
    for i in range(len(array[-1])):
        if array[-1][i] == 2:
            return i


def ladder(array):
    x = len(array) - 1
    y = find_destination(array)
    direction = 2

    dx = [0, 0, -1]
    dy = [1, -1, 0]

    while True:
        if x == 0:
            return y

        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 100 and 0 <= ny < 100 and array[nx][ny] != 0:
                array[x][y] = 0
                x = nx
                y = ny


for tc in range(1, 11):
    n = int(input())
    array = [list(map(int,input().split())) for _ in range(100)]
    print(f'#{n} {ladder(array)}')

