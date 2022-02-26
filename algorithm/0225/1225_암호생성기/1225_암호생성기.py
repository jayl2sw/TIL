from collections import deque
import sys

sys.stdin = open('input.txt')


for tc in range(1, 11):
    n = int(input())
    q = deque(list(map(int, input().split())))
    idx = 1
    while True:
        q.append(q.popleft() - idx)
        if q[-1] <= 0:
            q[-1] = 0
            break
        idx += 1
        if idx == 6:
            idx = 1

    print(f'#{tc}', *q)

