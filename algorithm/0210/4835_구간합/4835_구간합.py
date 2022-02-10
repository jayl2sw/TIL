import sys

sys.stdin = open('sample_input.txt')


def biggest_sum(m, array):
    sum_array = []
    for i in range(len(array)-m+1):
        sum_array.append(sum(array[i:i+m]))
    return max(sum_array) - min(sum_array)


T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    print(f'#{tc} {biggest_sum(m, array)}')

