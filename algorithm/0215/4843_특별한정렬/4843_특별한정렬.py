import sys

sys.stdin = open('input.txt')

def wierd_sort(array):
    array.sort()
    result = []
    for i in range(5):
        result.append(array[-i-1])
        result.append(array[i])
    return result


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    array = list(map(int, input().split()))
    print(f'#{tc}', end=' ')
    for i in range(10):
        print(wierd_sort(array)[i], end=' ')
    print()
