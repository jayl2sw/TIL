import sys

sys.stdin = open('input.txt')


def solution(array):
    total = 0
    count = 0
    for i in range(len(array)-1):
        if array[i] == '(':
            if array[i+1] == ')':
                total += count
            else:
                count += 1

        else:
            if array[i+1] == ')':
                total += 1
                count -= 1
    return total

T = int(input())
for tc in range(1, T+1):
    array = list(input())
    print(f'#{tc} {solution(array)}')