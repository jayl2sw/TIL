import sys

sys.stdin = open('input.txt')

def times(start, end, target):
    count = 0
    while True:
        count += 1
        middle = (start + end) // 2
        if middle == target:
            return count
        elif middle < target:
            start = middle
        else:
            end = middle

def findWinner(A, B):
    if A < B:
        return 'A'
    elif A == B:
        return 0
    else:
        return 'B'
T = int(input())

for tc in range(1, T+1):
    N, targetA, targetB = map(int, input().split())
    A = times(1, N, targetA)
    B = times(1, N, targetB)

    print(f'#{tc} {findWinner(A, B)}')


