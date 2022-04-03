import sys
sys.stdin = open('input.txt')

INF = int(1e6)

def dijkstra():
    visited = [False] * (V+1)
    cost = [INF] * (V + 1)
    cost[0] = 0


    for _ in range(V):
        min_idx = -1
        min_value = INF
        for i in range(V+1):
            if not visited[i] and min_value > cost[i]:
                min_idx = i
                min_value = cost[i]

        visited[min_idx] = True

        for j in range(V+1):
            if cost[j] > cost[min_idx] + graph[min_idx][j]:
                cost[j] = cost[min_idx] + graph[min_idx][j]

    return cost[V]


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[INF] * (V+1) for _ in range(V+1)]

    for _ in range(E):
        s, e, w = map(int,input().split())
        graph[s][e] = w

    print(f'#{tc} {dijkstra()}')