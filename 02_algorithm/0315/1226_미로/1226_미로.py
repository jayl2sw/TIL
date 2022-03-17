from collections import deque
import sys
sys.stdin = open('input.txt')


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def check(x, y):
    if x < 0 or x > 15 or y < 0 or y > 15:
        return False
    return True


def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if check(nx, ny) and data[nx][ny] == 0:
                data[nx][ny] = data[x][y] + 1
                q.append((nx, ny))

            elif check(nx, ny) and data[nx][ny] == 2:
                return 1
    return 0



for tc in range(1, 11):
    N = int(input())
    data = [list(map(int, input())) for _ in range(16)]

    for i in range(16):
        for j in range(16):
            if data[i][j] == 3:
                x, y = i, j
    result = bfs(x, y)
    print(f'#{tc} {result}')
