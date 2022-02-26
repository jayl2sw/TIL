from collections import deque
import sys

sys.stdin = open('input.txt')

def bfs(start):
    q = deque()
    q.append(start)
    visited = []

    while q:
        n = q.popleft()
        print(n, end=' ')
        visited.append(n)

        for nxt in graph[n]:
            if nxt not in visited and nxt not in q:
                q.append(nxt)



E, V = map(int, input().split())
graph = [[] for _ in range(E+1)]
array = list(map(int, input().split()))

for i in range(8):
    graph[array[2*i]].append(array[2*i+1])

print(graph)
bfs(1)

