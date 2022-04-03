import sys
from collections import deque
sys.stdin = open('input.txt')


def bfs(start):
    q = deque()
    q.append(start)

    while q:
        now = q.popleft()
        visited[now] = True
        print(now, end=' ')
        for nxt in graph[now]:
            if not visited[nxt] and nxt not in q:
                q.append(nxt)


arr = list(map(int,input().split()))
graph = [[] for _ in range(8)]
for i in range(len(arr)//2):
    graph[arr[2*i]].append(arr[2*i+1])
    graph[arr[2*i+1]].append(arr[2*i])
visited = [False] * 8
bfs(1)
