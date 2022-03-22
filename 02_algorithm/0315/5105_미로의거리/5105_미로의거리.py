from collections import deque
import sys
sys.stdin = open('input.txt')


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def check(x, y):
    if x < 0 or x > N - 1 or y < 0 or y > N - 1:
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

            # 2에서 1더하면 3이 되어버려서 출발지를 3으로 도착지를 2로 함
            if check(nx, ny) and data[nx][ny] == 0:
                data[nx][ny] = data[x][y] + 1
                q.append((nx, ny))

            elif check(nx, ny) and data[nx][ny] == 2:
                data[nx][ny] = data[x][y] - 3
                return data[nx][ny]
    return 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if data[i][j] == 3:
                x, y = i, j

    print(f'#{tc} {bfs(x, y)}')