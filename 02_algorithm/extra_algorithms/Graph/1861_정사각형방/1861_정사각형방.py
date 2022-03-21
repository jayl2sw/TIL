import sys

sys.stdin = open('input.txt')
from pprint import pprint
from collections import deque


def bfs(x, y):
    q = []
    s = []
    q.append((x, y))
    v[x][y] = 1
    s.append(arr[x][y])

    while q:
        cx, cy = q.pop()
        for direct in range(4):
            nx, ny = cx + dx[direct], cy + dy[direct]
            if 0 <= nx < N and 0 <= ny < N and v[nx][ny] == 0 and abs(arr[cx][cy] - arr[nx][ny]) == 1:
                q.append((nx, ny))
                v[nx][ny] = 1
                s.append(arr[nx][ny])

    return min(s), len(s)


T = int(input())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for tcase in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [[0] * N for _ in range(N)]
    min_num = 0
    cnt = 0
    for i in range(N):
        for j in range(N):
            if v[i][j] == 0:
                tn, tc = bfs(i, j)
                if cnt < tc or cnt == tc and min_num > tn:
                    cnt = tc
                    min_num = tn
    print(f'#{tcase} {min_num} {cnt}')
