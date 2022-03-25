import sys
sys.stdin = open('input.txt')
def dfs(ci, cj, k, v):
    global result
    if k > 3:
        return
    if k == 3 and ci == si and cj == sj and result < len(v):
        result = len(v)
        return

    di, dj = (1, 1, -1, -1, 1), (1, -1, -1, 1, 1)
    for i in range(k, k+2):
        ni, nj = ci + di[i], cj + dj[i]
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] not in v:
            v.append(arr[ni][nj])
            dfs(ni, nj, i, v)
            v.pop()



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = -1
    for si in range(N):
        for sj in range(N):
            dfs(si, sj, 0, [])

    print(f'#{tc} {result}')

