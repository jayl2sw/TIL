import sys
sys.stdin = open('input.txt')


def construct_candidator(arr, k, N, c, visited):
    for i in range(N):
        if i not in visited:
            c[i] = arr[k][i]
    return

# arr: input.txt array
# k: 현재 더해야 할 행의 index
# n: arr의 행 수
# total: n-1행까지 더한 총 값
# visited: 지금까지 조사한 열 index들의 list

def min_total(arr, k, n, total, visited):
    global min_v
    if total >= min_v:
        return

    if k == n:
        min_v = total
        return

    c = [0] * MAXCANDIDATES
    construct_candidator(arr, k, n, c, visited)
    for i in range(n):
        if c[i] != 0:
            min_total(arr, k+1, n, total + c[i], visited+[i])


T = int(input())
for tc in range(1, T+1):
    MAXCANDIDATES = 10
    n = int(input())
    array = [list(map(int,input().split())) for _ in range(n)]
    min_v = int(1e9)

    min_total(array, 0, n, 0, [])
    print(f'#{tc} {min_v}')




