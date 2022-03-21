import sys

sys.stdin = open('input.txt')


def DFS(n, ssum):
    global ans

    if ssum >= B+ans:
        return
    if n == N:
        if ssum >= B and ans > ssum - B:
            ans = ssum - B
        return ans

    DFS(n + 1, ssum + lst[n])
    DFS(n + 1, ssum)


T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    lst = list(map(int, input().split()))
    ans = 12345678
    DFS(0, 0)
    print(f'#{tc} {ans}')
