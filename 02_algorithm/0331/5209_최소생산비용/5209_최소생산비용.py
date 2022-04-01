def solution(i, N, visited, cost):
    global minCost
    if minCost < cost:
        return
    if i == N:
        minCost = cost

    for j in range(N):
        if not visited[j]:
            visited[j] = True
            solution(i+1, N, visited, cost + arr[i][j])
            visited[j] = False

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [False] * N
    minCost = int(1e9)
    solution(0, N, visited, 0)
    print(f'#{tc} {minCost}')

