import sys
sys.stdin = open('input.txt')


def construct_candidator(arr, k, N, c, visited):

    for i in range(N):
        if i not in visited:
            c[i] = arr[k][i]

    return N


def min_total(arr, k, n, total, visited):
    global cnt
    cnt += 1
    global min_v
    if k == n:
        if min_v > total:
            min_v = total
        return

    if total >= min_v:
        return

    c = [0] * 10
    construct_candidator(arr, k, n, c, visited)
    for i in range(n):
        if c[i] != 0:
            min_total(arr, k+1, n, total + c[i], visited+[i])


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    array = [list(map(int,input().split())) for _ in range(n)]
    min_v = int(1e9)
    cnt = 0
    min_total(array, 0, n, 0, [])
    cnt += 1
    print(f'#{tc} {min_v} \t count: {cnt}')




