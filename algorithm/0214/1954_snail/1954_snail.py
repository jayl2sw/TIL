import sys

sys.stdin = open("input.txt")

def snail(n):
    array = [[0] * n for _ in range(n)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    i = 2
    direction = 0
    x = 0
    y = 0
    array[0][0] = 1
    count = 1

    while count < int(n**2):
        nx = x + dx[direction]
        ny = y + dy[direction]

        if nx < 0 or ny < 0 or nx >= n or ny >= n or array[nx][ny]!= 0:
            direction += 1
            if direction == 4:
                direction = 0
            continue


        array[nx][ny] = i
        x = nx
        y = ny
        i += 1
        count += 1

    return array


T = int(input())

for tc in range(1, T+1):
    n = int(input())
    result = snail(n)
    print(f'#{tc}')
    for i in range(n):
        for j in range(n):
            print(result[i][j], end=' ')
        print()