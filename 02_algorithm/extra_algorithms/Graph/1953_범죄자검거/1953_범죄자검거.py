import sys
sys.stdin = open('input.txt')

def bfs(x, y):
    cnt = 0
    q = []
    q.append((1, x, y))

    while q:
        time, i, j = q.pop(0)
        if v[i][j] == 1:
            continue
        else:
            v[i][j] = 1
            cnt += 1
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != 0 and pipes[arr[i][j]][k] == 1 \
                    and pipes[arr[ni][nj]][opp[k]] == 1 and v[ni][nj] == 0 and time < L:
                q.append((time + 1, ni, nj))

    return cnt


T = int(input())
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [[0] * M for _ in range(N)]

    opp = [1, 0, 3, 2]
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    pipes = [[],
             [1, 1, 1, 1],
             [1, 1, 0, 0],
             [0, 0, 1, 1],
             [1, 0, 0, 1],
             [0, 1, 0, 1],
             [0, 1, 1, 0],
             [1, 0, 1, 0]]


    print(f'#{tc} {bfs(R, C)}')

