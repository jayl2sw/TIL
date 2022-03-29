import sys
sys.stdin = open('input.txt')

def solution(i, j, total):
    global minTotal
    if total >= minTotal:
        return

    if i == N-1 and j == N-1:
        minTotal = total

    for di, dj in ((1, 0), (0, 1)):
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < N:
            solution(ni, nj, total + arr[ni][nj])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    minTotal = 1e9
    solution(0, 0, arr[0][0])
    print(f'#{tc} {minTotal}')