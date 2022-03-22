from collections import deque

import sys
sys.stdin = open('input.txt')


def bfs(start, goal):
    q = deque()
    # (start 로부터의 거리, 현재 노드)
    q.append((0, start))
    visited.append(start)
    while q:
        cost, node = q.popleft()
        visited.append(node)
        if node == goal:
            return cost
        # 해당 노드에서 다음으로 갈 수 있는 노드 중, visited에 없는 것
        for nxt in graph[node]:
            if nxt not in visited:
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

    print(graph)
    # Start, Goal
    S, G = map(int, input().split())

    visited = []
    print(f'#{tc} {bfs(S,G)}')


