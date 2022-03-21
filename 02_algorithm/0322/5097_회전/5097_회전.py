T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    result = arr[(m)%n]
    print(f'#{tc} {result}')