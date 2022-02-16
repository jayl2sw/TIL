import sys
sys.stdin = open('input.txt')


def hoarding(n, array):
    result = 0
    for idx in range(n-1):
        max_price = max(array[idx + 1:])
        if array[idx] < max_price:
            result += (max_price - array[idx])

    return result


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    array = list(map(int, input().split()))
    print(f'#{tc} {hoarding(n, array)}')

