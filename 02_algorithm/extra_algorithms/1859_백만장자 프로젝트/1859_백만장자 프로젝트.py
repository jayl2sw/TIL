import sys
sys.stdin = open('input.txt')


def hoarding(n, array):
    result = array[:]
    max_v = 0
    for i in range(len(array)-1, -1, -1):
        if array[i] > max_v:
            max_v = array[i]
        result[i] = max_v
    return sum(result) - sum(array)


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    array = list(map(int, input().split()))
    print(f'#{tc} {hoarding(n, array)}')

