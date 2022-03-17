from collections import deque
import sys

sys.stdin = open("input.txt")
T = int(input())

def subtree(tree, N):
    q = deque()
    q.append(N)
    count = 1

    while q:
        now = q.popleft()
        for nxt in tree[now]:
            q.append(nxt)
            count += 1

    return count

for tc in range(1, T+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))

    tree = [[] for _ in range(E+2)]
    for i in range(E):
        tree[arr[2*i]].append(arr[2*i+1])

    print(tree)
    result = subtree(tree, N)
    print(f'#{tc} {result}')



