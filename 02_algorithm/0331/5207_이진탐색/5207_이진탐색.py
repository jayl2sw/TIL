import sys
sys.stdin = open("input.txt")


def binarySearch(target):
    global cnt

    l = 0
    r = N-1
    result = []
    while l <= r:
        m = (l + r) // 2
        if A[m] == target:
            print(A[m], result)
            for i in range(1, len(result)):
                if result[i] == result[i-1]:
                    return
            cnt += 1
            return
        elif A[m] > target:
            r = m - 1
            if result[-1] == 'l':
                return
            result.append('l')
        else:
            l = m + 1
            result.append('r')
    return


T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    A = sorted(list(map(int,input().split())))
    B = list(map(int,input().split()))
    cnt = 0

    for number in B:
        binarySearch(number)

    print(f'#{tc} {cnt}')