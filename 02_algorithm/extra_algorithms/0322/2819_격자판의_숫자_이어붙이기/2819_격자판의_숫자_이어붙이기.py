
def bfs(i, j):
    temp = [[set() for i in range(4)] for j in range(4)]

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]

        if 0 <= ni < 4 and 0 <= nj < 4:
            for now in temp[i][j]:
                now = arr[ni][nj] + now






T = int(input())
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]


for tc in range(1, T+1):
    arr = [list(input().split()) for _ in range(4)]

    v = []
    for i in range(4):
        for j in range(4):
            bfs(i, j)

    print(len(v))
