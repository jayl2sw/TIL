import sys
sys.stdin = open('input.txt')

def solution(i, p):
    global maxP
    if maxP > p:
        return

    if i == N:
        maxP = p

    for j in range(N):
        if not Done[j] and arr[i][j]:
            Done[j] = True
            solution(i+1, p * arr[i][j])
            Done[j] = False


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(lambda x:x / 100, map(int, input().split()))) for _ in range(N)]
    Done = [False] * N
    maxP = 0

    solution(0, 1)
    result = maxP*100
    print(f'#{tc} {result:.6f}')