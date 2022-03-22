import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    D, M, Q, Y = map(int, input().split())
    schedule = [0] + list(map(int, input().split()))


    d = [0] * 13
    d[1] = min(D * schedule[1], M)
    d[2] = d[1] + min(D * schedule[2], M)
    for month in range(3, 13):
        d[month] = min(d[month-1] + D * schedule[month], d[month-1] + M, d[month-3] + Q)

    print(f'#{tc} {min(d[12], Y)}')

