def prim(start, V):
    MST = [0] * (V+1)
    key = [10000] * (V+1)
    key[start] = 0

    for _ in range(V):
        u = 0
        minV = 10000
        for i in range(V+1):
            if MST[i] == 0 and key[i] < minV:
                u = i
                minV = key[i]
        MST[u] = 1

        for v in range(V+1):
            if MST[v] == 0 and adjM[u][v]  > 0:
                return
            
V, E = map(int,input().split())
adjM = [[0] *(V+1) for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int,input().split())
    adjM[u][v] = w
    adjM[v][u] = w


