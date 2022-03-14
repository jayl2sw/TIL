import sys

sys.stdin = open('input.txt')

def ruins(array):
    cnt = 0
    max_cnt = 0
    for i in range(n):
        for j in range(m):
            if array[i][j]:
                cnt += 1
                if cnt > max_cnt:
                    max_cnt = cnt
            else:
                cnt = 0
    cnt = 0
    for j in range(m):
        for i in range(n):
            if array[i][j]:
                cnt += 1
                if cnt > max_cnt:
                    max_cnt = cnt
            else:
                cnt = 0
    return max_cnt

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    array = [list(map(int,input().split())) for _ in range(n)]
    print(f'#{tc} {ruins(array)}')
