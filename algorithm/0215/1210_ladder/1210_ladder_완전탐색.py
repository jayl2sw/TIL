import sys

sys.stdin = open('input.txt')


def find_start(array):
    result = []
    for i in range(len(array)):
        if array[0][i] == 1:
            result.append(i)
    return result


def ladder(start, array):
    dx = [0, 0, 1]
    dy = [-1, 1, 0]
    direction = 2 #0일 경우 좌측, 1일

    x = 0
    y = start
    while True:
        if x == 99:
            if array[x][y] == 2:
                return True
            else:
                return False

        if direction == 2:
            for i in range(3):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= 100 or ny >= 100:
                    continue

                if array[nx][ny] != 0:
                    x = nx
                    y = ny
                    direction = i
                    break

        else:
            nx = x + dx[direction]
            ny = y + dy[direction]

            if nx < 0 or ny < 0 or nx >= 100 or ny >= 100 or array[nx][ny] == 0:
                direction = 2
                x += 1
                y = y

            else:
                x = nx
                y = ny


for tc in range(1, 11):
    n = int(input())
    array = [list(map(int, input().split())) for _ in range(100)]
    starts = find_start(array)
    for start in starts:
        if ladder(start, array):
            print(f'#{tc} {start}')
