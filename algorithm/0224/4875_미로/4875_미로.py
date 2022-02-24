import sys
sys.stdin = open('input.txt')


def start(N, array):
    # 출발점 찾기
    for i in range(N):
        for j in range(N):
            if array[i][j] == 3:
                return maze(N, array, i, j)


def maze(N, array, r, c):
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr < 0 or nc < 0 or nr >= N or nc >= N:
            continue

        if array[nr][nc] == 2:
            return 1

        if array[nr][nc] == 0 and [nr, nc] not in visited:
            visited.append([r, c])
            if maze(N, array, nr, nc):
                return 1
    return 0


T = int(input())
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

for tc in range(1, T+1):
    N = int(input())
    array = [list(map(int, input())) for _ in range(N)]
    visited = []
    success = start(N, array)
    print(f'#{tc} {success}')