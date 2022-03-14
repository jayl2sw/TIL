import sys
sys.stdin = open('input.txt')

def dfs(start):
    visited.append(start)
    for node in graph[start]:
        if node not in visited:
            dfs(node)


for tc in range(1, 11):
    n, v = map(int,input().split())
    graph = [[] for _ in range(100)]
    visited = []
    array = list(map(int,input().split()))
    for i in range(0, 2*v, 2):
        graph[array[i]].append(array[i+1])
    dfs(0)
    if 99 in visited:
        result = 1
    else:
        result = 0
    print(f'#{tc} {result}')