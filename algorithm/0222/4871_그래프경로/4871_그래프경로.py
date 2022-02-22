import sys
sys.stdin = open('input.txt')

def dfs(start):
    visited.append(start)
    for node in graph[start]:
        if node not in visited:
            dfs(node)


T = int(input())
for tc in range(1, T+1):
    visited = []
    v, e = map(int, input().split())
    graph = [[] for i in range(v+1)]
    for i in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
    s, g = map(int,input().split())
    dfs(s)
    if g in visited:
        result = 1
    else:
        result = 0

    print(f'#{tc} {result}')