import sys
sys.stdin = open('input.txt')


def dfs(start, graph):
    visited.append(start)
    print(start, end=' ')
    for node in graph[start]:
        if node not in visited:
            dfs(node, graph)


n, k = map(int, input().split())
array = list(map(int, input().split()))
visited = []
graph = [[] for _ in range(n + 1)]
for i in range(0, 2 * k, 2):
    graph[array[i]].append(array[i + 1])
    graph[array[i + 1]].append(array[i])
print(graph)

dfs(1, graph)
