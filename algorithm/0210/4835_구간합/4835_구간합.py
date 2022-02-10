import sys

sys.stdin = open('sample_input.txt')


def max(set):
    max_val = -int(1e9)
    for i in set:
        if max_val < i:
            max_val = i
    return max_val


def min(set) :
    min_val = int(1e9)
    for i in set:
        if min_val > i:
            min_val = i
    return min_val


def sum(array):
    total = 0
    for i in array:
        total += i
    return total


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

