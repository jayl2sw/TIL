import sys
sys.stdin = open('input.txt')


def check(array):
    d = [0] * 10

    # triplet 확인
    for idx in array:
        d[idx] += 1
    if 3 in d:
        return True

    # run 확인
    for idx in range(1, 10):
        if d[idx] >= 1:
            d[idx] = 1 + d[idx-1]
            if d[idx] == 3:
                return True

    # 둘 다 없음
    return False

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    p1 = []
    p2 = []
    result = 0
    for i in range(len(arr)):
        if i % 2:
            p2.append(arr[i])
            if check(p2):
                result = 2
                break
        else:
            p1.append(arr[i])
            if check(p1):
                result = 1
                break

    print(f'#{tc} {result}')

