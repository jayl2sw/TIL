import sys

sys.stdin = open('input.txt')

def check(array):
    for i in range(9):
        if sum(array[i]) != 45:
            return 0
        sub_total = 0
        for j in range(9):
            sub_total += array[j][i]
        if sub_total != 45:
            return 0

    for a in range(3):
        for b in range(3):
            sub_total = 0
            for i in range(3):
                for j in range(3):
                    sub_total += array[a*3+i][b*3+j]
            if sub_total!=45:
                return 0
    return 1


T = int(input())
for tc in range(1,T+1):
    array = [list(map(int,input().split())) for _ in range(9)]
    result = check(array)
    print(f'#{tc} {result}')