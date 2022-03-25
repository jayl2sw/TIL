import sys
sys.stdin = open('input.txt')

def dfs(i, j, n, result):
    if n == 7:
        sset.add(result)
        return

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < 4 and 0 <= nj < 4:
            dfs(ni, nj, n+1, result*10+arr[ni][nj])

T = int(input())
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    sset = set()
    for si in range(4):
        for sj in range(4):
            dfs(si, sj, 0, 0)

    print(len(sset))
