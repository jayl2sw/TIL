import sys
sys.stdin = open("input.txt")


def kill(n, m, array):
    max_t = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            total = 0
            for a in range(m):
                for b in range(m):
                    total += array[i+a][j+b]
            if total > max_t:
                max_t = total
    return max_t

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    print(f'#{tc} {kill(n,m,arr)}')

