import sys

sys.stdin = open('input.txt')

def bigger(array, n):
    cnt = 1
    max_cnt = 1
    for idx in range(1, n):
        if array[idx] > array[idx-1]:
            cnt += 1
            if max_cnt < cnt:
                max_cnt = cnt
        else:
            cnt = 1
    return max_cnt

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    array = list(map(int,input().split()))
    print(f'#{tc} {bigger(array, n)}')
