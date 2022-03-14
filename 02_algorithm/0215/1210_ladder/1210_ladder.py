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

        if direction == 2:
            for i in range(3):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= 100 or ny >= 100:
                    continue

                if array[nx][ny] == 1:
                    x = nx
                    y = ny
                    direction = i
                    break

        else:
            nx = x + dx[direction]
            ny = y + dy[direction]

            if nx < 0 or ny < 0 or nx >= 100 or ny >= 100 or array[nx][ny] == 0:
                direction = 2
                x = x - 1
                y = y

            else:
                x = nx
                y = ny


for tc in range(1, 11):
    n = int(input())
    array = [list(map(int,input().split())) for _ in range(100)]
    print(f'#{n} {ladder(array)}')

