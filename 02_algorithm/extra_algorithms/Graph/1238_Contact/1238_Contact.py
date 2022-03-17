import sys
from collections import deque

sys.stdin = open('input.txt')

for tc in range(1, 11):
    N, start = map(int, input().split())
    arr = list(map(int,input().split()))
    graph = [[] for _ in range(101)]
    for i in range(N//2):
        graph[arr[i*2]].append(arr[i*2+1])

    contacted = []
    latest = 0
    latest_arr = []

    q = deque()
    q.append((0, start))

    while q:
        time, now = q.popleft()
        if now in contacted:
            continue
        if latest < time:
            latest = time
            latest_arr = []
        contacted.append(now)
        latest_arr.append(now)
        for nxt in graph[now]:
            if nxt not in contacted:
                q.append((time + 1, nxt))

    result = max(latest_arr)

    print(f'#{tc} {result}')





