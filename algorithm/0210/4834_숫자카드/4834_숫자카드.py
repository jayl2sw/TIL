import sys

sys.stdin = open('sample_input.txt')


def mode(array):
    d = [0] * 10
    for number in array:
        d[number] += 1

    count = max(d)
    number = 10 - d[::-1].index(count) - 1
    return number, count


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    array = list(map(int, input()))
    result = mode(array)
    print(f'#{tc} {result[0]} {result[1]}')
