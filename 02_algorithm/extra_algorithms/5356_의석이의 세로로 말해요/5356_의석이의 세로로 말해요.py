import sys
sys.stdin = open('input.txt')


def find_max_length(array):
    result = max([len(array[i]) for i in range(5)])
    return result

def vertical(array):
    for j in range(find_max_length(array)):
        for i in range(5):
            if len(array[i]) > j:
                print(array[i][j], end='')
T = int(input())
for tc in range(1, T+1):
    array = [input() for _ in range(5)]

    print(f'#{tc}', end=' ')
    vertical(array)
    print()