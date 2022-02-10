import sys

sys.stdin = open('sample_input.txt')

def counting_sort(array):
    N = len(array)
    counters = [0] * (int(1e6) + 1)
    temp = [0] * N
    for number in array:
        counters[number] += 1

    for i in range(1, len(counters)):
        counters[i] += counters[i - 1]

    for i in range(N - 1, -1, -1):
        temp[counters[array[i]] - 1] = array[i]
        counters[array[i]] -= 1

    return temp


def minmax(array):
    array = counting_sort(array)
    return array[-1] - array[0]


T = int(input())
for i in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    print(f'#{i} {minmax(numbers)}')
