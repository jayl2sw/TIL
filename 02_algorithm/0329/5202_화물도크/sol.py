import sys
sys.stdin = open('input.txt')

T = int(input())
# cur 뒤에 올 수 있는 스케줄 개수
def recur(cur):
    if dp[cur] != -1:
        return dp[cur]

    ret = 0

    for i in range(n):
        # 다음에 올 수 있는 것들 돌면서
        if cur <= arr[i][0]:
            # 현재 ret와 새로 찾은 ret 중 더 큰 것을 ret으로 바꿈
            ret = max(ret, recur(arr[i][1]) + 1)
            dp[cur] = ret
            print(dp)

    return ret


for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    print(arr)
    dp = [-1 for _ in range(25)]

    print(f'#{tc} {recur(0)}')