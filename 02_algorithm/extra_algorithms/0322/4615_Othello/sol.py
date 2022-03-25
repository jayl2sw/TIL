import sys

sys.stdin = open('input.txt')

opp = [0, 2, 1]

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [[0] * (N + 1) for _ in range(N + 1)]
    # 시작
    arr[N // 2][N // 2 + 1] = arr[N // 2 + 1][N // 2] = 1
    arr[N // 2][N // 2] = arr[N // 2 + 1][N // 2 + 1] = 2
    print(arr)
    for _ in range(M):
        i, j, p = map(int, input().split())

        print('i,j,p:', i, j, p)
        arr[i][j] = p
        for di, dj in ((1, 1), (0, 1), (-1, 1), (-1, 0), (1, 0), (1, -1), (0, -1), (-1, -1)):
            k = 1
            c = []
            while k < len(arr) - 1:
                if 0 < i + k * di <= N and 0 < j + k * dj <= N:
                    if arr[i + k * di][j + k * dj] == 0:
                        print('#1', i + k * di, j + k * dj, arr[i + k * di][j + k * dj])
                        c = []
                        break
                    elif arr[i + k * di][j + k * dj] == opp[p]:
                        c.append([i + k * di, j + k * dj])
                        print('#2', i + k * di, j + k * dj, arr[i + k * di][j + k * dj])
                    else:
                        if c:
                            for ci, cj in c:
                                arr[ci, cj] = p
                        print('#3', i + k * di, j + k * dj, arr[i + k * di][j + k * dj])
                k += 1
            print(arr)
