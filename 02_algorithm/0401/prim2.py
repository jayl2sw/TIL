def prim2(start, V):
    MST = [0]* (V+1)
    MST[start] = 1
    cost = 0
    for _ in range(V):
        u = 0
        minV = 10000
        for i in range(V+1):
            if MST[i] == 1:
                for j in range(V+1):
                    if 0< graph[i][j] < minV and MST[j] == 0:
                        u = j
                        minV = graph[i][j]
        cost += minV
        MST[u] =1

V, E = map(int,input().split())
graph = [[0] *(V+1) for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int,input().split())
    graph[u][v] = w
    graph[v][u] = w