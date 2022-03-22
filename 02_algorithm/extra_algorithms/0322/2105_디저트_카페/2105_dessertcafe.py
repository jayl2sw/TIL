T = int(input())
for tc in range(1, T+1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    di = [1, 1, -1, -1]
    dy = [1, -1, 1, -1]
    