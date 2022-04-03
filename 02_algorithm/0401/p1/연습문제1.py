import sys
sys.stdin = open('input.txt')


def dfs(start):
    visited[start] = True
    print(start, end=' ')
    for nxt in graph[start]:
        if not visited[nxt]:
            dfs(nxt)


arr = list(map(int,input().split()))
graph = [[] for _ in range(8)]
for i in range(len(arr)//2):
    graph[arr[2*i]].append(arr[2*i+1])
    graph[arr[2*i+1]].append(arr[2*i])
visited = [False] * 8
dfs(1)
