import sys
sys.stdin = open("input.txt")


# def times(list):
#     array = [0] * 201
#     for move in list:
#         start = (min(move[0], move[1])+1) //2
#         end = (max(move[0], move[1])+1) //2
#         for i in range(start, end+1):
#             array[i] += 1
#
#     return max(array)

def times(list):
    array = [0] * 401
    for move in list:
        start = min(move[0], move[1])
        end = max(move[0], move[1])
        for i in range(start, end+1):
            array[i] += 1

    return max(array)


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    print(f'#{tc} {times(arr)}')

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    print(f'#{tc} {times(arr)}')

