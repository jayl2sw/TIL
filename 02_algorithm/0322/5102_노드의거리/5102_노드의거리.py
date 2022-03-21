from collections import deque

import sys
sys.stdin = open('input.txt')


def bfs(start, goal):
    q = deque()
    q.append((0, start))
    visited.append(start)
    while q:
        cost, node = q.popleft()
        visited.append(node)
        if node == goal:
            return cost
        for nxt in graph[node]:
            if nxt not in visited and nxt not in q:
                q.append((cost+1, nxt))

    return 0


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())

    graph = [[] for _ in range(V+1)]
    for i in range(E):
        n1, n2 = map(int, input().split())
        graph[n1].append(n2)
        graph[n2].append(n1)

    S, G = map(int, input().split())

    visited = [0]*(V+1)
    print(f'#{tc} {bfs(S,G)}')


