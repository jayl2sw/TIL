import sys
from pprint import pprint
sys.stdin = open('input.txt')

def dfs(start):
    stack = []
    visited = [False] * (V+1)
    visited[start] = True

    while start != 0:
        for next in range(1, V+1):
            if G[start][next] == 1 and not visited[next]:
                stack.append(start)
                start = next
                visited[start] = True
                break
        else:
            if stack:
                start = stack.pop()
            else:
                start = 0

V, E = map(int, input().split())
data = list(map(int, input().split()))

print(data)
G = [[0]* (V+1)  for _ in range(V+1)]

pprint(G)
for i in range(V+1):
    G[data[i * 2]][data[i * 2 + 1]] = 1
    G[data[i * 2 + 1]][data[i * 2]] = 1

dfs(1)