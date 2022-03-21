T =  int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    graph = [[0] * (N+1) for _ in range(N+1)]
    for _ in range(M):
        i, j, player = map(int, input.split())
        # 8방향 체크
        # 뒤집을게 있으면
        # 뒤집는다.

