opp = ['', 2, 1]


# di, dj는 1 or -1
def check(start_i, start_j, player):
    for di in range(-1, 2):
        for dj in range(-1, 2):
            i = start_i
            j = start_j
            v = []
            if di == 0 and dj == 0:
                continue
            while True:
                ni = i + di
                nj = j + dj
                if ni > N or ni < 1 or nj > N or nj < 1:
                    break
                if graph[ni][nj] == player:
                    for location in v:
                        x, y = location
                        if graph[x][y] == opp[player]:
                            graph[x][y] = player
                    break

                i = ni
                j = nj
                v.append((i,j))



T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    graph = [[0] * (N+1) for _ in range(N+1)]
    graph[N // 2][N // 2] = 2
    graph[N // 2 + 1][N // 2 + 1] = 2
    graph[N // 2][N // 2 + 1] = 1
    graph[N // 2 + 1][N // 2] = 1

    for _ in range(M):
        i, j, player = map(int, input().split())
        graph[i][j] = player
        check(i, j, player)

    cnt1 = 0
    cnt2 = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if graph[i][j] == 1:
                cnt1 += 1
            elif graph[i][j] == 2:
                cnt2 += 1
    print(f'#{tc} {cnt1} {cnt2}')
