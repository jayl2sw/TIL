import sys

sys.stdin = open('input.txt')


def dfs(n, i, j, v, cnt):
    global ans
    if n > 3:
        return

    if n == 3 and i == si and j == sj and ans < cnt:
        ans = cnt
        return

    for k in range(n, n + 2):
        ni, nj = i + di[k], j + dj[k]
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] not in v:
            dfs(k, ni, nj, v + [arr[ni][nj]], cnt + 1)


di = [1, 1, -1, -1, 1]
dj = [1, -1, -1, 1, 1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = -1
    for si in range(N):
        for sj in range(N):
            dfs(0, si, sj, [], 0)

    print(ans)
