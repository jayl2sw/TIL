import sys
sys.stdin = open("input.txt")
T = int(input())
opp = [0, 2, 1]

for tc in range(1, T+1):
    N, M = map(int, input().split())

    arr = [[0]*(N+1) for _ in range(N+1)]
    arr[N // 2][N // 2] = arr[N // 2 + 1][N // 2 + 1] = 2
    arr[N // 2][N // 2 + 1] = arr[N // 2 + 1][N // 2] = 1

    for _ in range(M):
        i, j, p = map(int,input().split())
        arr[i][j] = p
        for di, dj in ((1, -1),(1, 0),(1, 1),(0, 1),(-1, 1),(-1, 0),(-1, -1),(0, -1)):
            s = []
            k = 1
            while True:
                ni, nj = i + di * k, j + dj * k
                if 0 < ni <= N and 0 < nj <= N:
                    if arr[ni][nj] == 0:
                        break
                    elif arr[ni][nj] == opp[p]:
                        s.append((ni, nj))
                        k += 1
                    elif arr[ni][nj] == p:
                        for location in s:
                            arr[location[0]][location[1]] = p
                        break
                else:
                    break

    print(arr)
    r1 = 0
    r2 = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if arr[i][j] == 1:
                r1 += 1
            elif arr[i][j] == 2:
                r2 += 1

    print(f'#{tc} {r1} {r2}')

