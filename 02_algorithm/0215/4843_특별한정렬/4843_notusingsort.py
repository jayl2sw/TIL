import sys

sys.stdin = open('input.txt')

def wierd_sort():
    for _ in range(5):
        max_v = 0
        min_v = int(1e9)
        for i in array:
            if i > max_v:
                max_v = i
            if i < min_v:
                min_v = i

        print(max_v, end=' ')
        array.remove(max_v)
        print(min_v, end=' ')
        array.remove(min_v)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    array = list(map(int, input().split()))
    print(f'#{tc}', end=' ')
    wierd_sort()
    print()

