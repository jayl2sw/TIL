import sys
sys.stdin = open("input.txt")

# 현재상황에서 가장 얻을 수 있는 높은 확률
def solution(employee, tasks):
    if tasks == (1 << N) - 1: # 모든 작업 수행 완료
        return 1

    if dp[tasks]:
        return dp[tasks]

    for i in range(N):
        if arr[employee][i] and not (tasks & (1 << i)):
            dp[tasks] = max(dp[tasks], arr[employee][i] * solution(employee+1, tasks ^ (1 << i)))

    return dp[tasks]

for tc in range(1, 1 + int(input())):
    N = int(input())
    arr = [list(map(lambda x: x / 100, map(int, input().split()))) for _ in range(N)]
    dp = [0] * (1 << N)

    result = solution(0, 0) * 100
    print(f'#{tc} {result:.6f}')