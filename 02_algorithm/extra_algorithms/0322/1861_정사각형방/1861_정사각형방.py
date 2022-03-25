import sys
sys.stdin = open("input.txt")
# sys.stdin = open("test.txt")

def dfs(ci, cj, cnt):
    global maxLength
    global maxLocation

    if d[ci][cj] != 0:
        if cnt >= d[ci][cj]:
            d[ci][cj] = cnt
        else:
            return


    for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        ni, nj = ci + di, cj + dj
        if 0 <= ni < N and 0 <= nj < N and arr[ci][cj] + 1 == arr[ni][nj]:
            dfs(ni, nj, cnt+1)

    if maxLength == cnt and arr[i][j] < arr[maxLocation[0]][maxLocation[1]] or maxLength < cnt:

        maxLength = cnt
        maxLocation = (i, j)




T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    maxLocation = (0, 0)
    maxLength = 0
    d = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            dfs(i, j, 1)

    print(f'#{tc} {arr[maxLocation[0]][maxLocation[1]]} {maxLength}')
