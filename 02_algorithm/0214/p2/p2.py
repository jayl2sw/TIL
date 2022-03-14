import sys

sys.stdin = open("input.txt")


def make_zero(array):
    count = 0
    for i in range(1 << 10):
        total = 0
        for j in range(10):
            if i & (1 << j):
                total += array[j]
        if total == 0:
            count +=1
            if count == 2:
                return 1
    return 0


T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    print(f'#{tc} {make_zero(arr)}')

