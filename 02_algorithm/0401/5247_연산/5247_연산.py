import sys
sys.stdin = open('input.txt')

from collections import deque


def bfs(N, M):
    q = deque()
    q.append((0, N))

    while q:
        time, now = q.popleft()
        if now == M:
            return time

        if 0 <= now <=1e6 and not d[now]:
            q.append((time + 1, now + 1))
            q.append((time + 1, now - 1))
            if now * 2 <= 1e6:
                q.append((time + 1, now * 2))
            q.append((time + 1, now - 10))
            d[now] = True

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().strip().split())
    d = [False] * (int(1e6)+1)
    print(f'#{tc} {bfs(N, M)}')