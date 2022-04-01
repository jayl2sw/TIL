import sys

sys.stdin = open('input.txt')


def pre(start):
    print(start, end=' ')
    for nxt in graph[start]:
        pre(nxt)


def mid(start):
    if graph[start]:
        mid(graph[start][0])
    print(start, end=' ')
    if len(graph[start]) == 2:
        mid(graph[start][1])


def post(start):
    for nxt in graph[start]:
        post(nxt)
    print(start, end=' ')


V, E = map(int, input().split())
arr = list(map(int, input().split()))
graph = [[] for _ in range(V + 1)]
for i in range(len(arr) // 2):
    graph[arr[2 * i]].append(arr[2 * i + 1])

print(graph)
pre(1)
print()
mid(1)
print()
post(1)
