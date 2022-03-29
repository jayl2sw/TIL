import sys
sys.stdin = open('input.txt')


# i: 지나온 개수, n : 최종 개수 total: 현재까지 비용
def solution(i, n, visited, total):
    global minTotal
    # 종료 조건 1포함해서 n개
    if i == n:
        # 마지막 노드에서 1로 가는 비용 추가 후
        total += arr[visited[-1]][1]
        if minTotal > total:
            # minTotal 업데이트
            minTotal = total

    # 1부터 N까지 돌면서
    for j in range(1, N+1):
        if j not in visited:
            solution(i+1, n, visited+[j], total + arr[visited[-1]][j])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * (N+1)] + [[0]+list(map(int, input().split())) for _ in range(N)] # 패딩
    minTotal = int(1e9)

    # 1번에서 출발
    solution(1, N, [1], 0)
    print(f'#{tc} {minTotal}')