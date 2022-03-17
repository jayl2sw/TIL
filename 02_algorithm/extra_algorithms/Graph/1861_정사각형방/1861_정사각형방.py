# import sys
# sys.stdin = open('input.txt')
from pprint import pprint
from collections import deque


def dfs(x, y):
    for dir in range(4):
        nx = i + dx[dir]
        ny = j + dy[dir]
        if 0 <= nx < N and 0 <= ny < N:
            if TF[nx][ny] == 1:
                TF[nx][ny] = TF[x][y] + 1
                dfs(nx, ny)


T = int(input())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for tc in range(1, T+1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    TF = [[0] * N for _ in range(N)]
    Max_V = 0
    Max_Num = 0
    max_xy = (0, 0)
    for i in range(N):
        for j in range(N):
            for dir in range(4):
                nx = i + dx[dir]
                ny = j + dy[dir]
                if 0 <= nx < N and 0 <= ny < N:
                    if graph[nx][ny] == graph[i][j] +1 or graph[nx][ny] == graph[i][j] - 1:
                        TF[i][j] = 1

    nums = []
    for i in range(N):
        for j in range(N):
            if TF[i][j] == 1:
                dfs(i, j)
                nums.append(graph[i][j])

    print(TF)
    print(nums)
