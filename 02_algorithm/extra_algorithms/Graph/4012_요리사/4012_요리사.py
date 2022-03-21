import sys
sys.stdin = open('input.txt')


# def make_sets():
#     set = [[]]
#     result = []
#     for i in range(1, N+1):
#         for j in range(len(set)):
#             temp = set[j]+[i]
#             if len(temp) < N//2:
#                 result.append(temp)
#                 set.append(temp)
#
#
#     return result
#
# def solutions(subset):
#     min_v = int(1e9)
#     for i in range(4):
#         for j in range(4):
#             if i < j:
#                 temp1 = arr[subset[i]][subset[j]] + arr[subset[j]][subset[i]]
#                 temp = list(set(subset) - {subset[i], subset[j]})
#                 temp2 = arr[temp[0]][temp[1]] + arr[temp[1]][temp[0]]
#                 result = abs(temp1 - temp2)
#                 if result < min_v:
#                     min_s = [[subset[i], subset[j]], temp]
#                     min_v = result
#
#     return min_v, min_s
# N은 짝수이다..

def calculate(materials):
    result = 0
    for material in materials:
        for i in range(N+1):
            if i in materials:
                result += arr[material][i]

    return result


# def make_sets():
#     sub_set = [[]]
#     result = []
#     for i in range(1, N+1):
#         for j in range(len(sub_set)):
#             temp = sub_set[j]+[i]
#             if len(temp) < N//2+0.5:
#                 sub_set.append(temp)
#                 if len(temp) > 1:
#                     result.append(set(temp))
#
#     return result

def make_sets():
    sub_set = [[]]
    result = []
    for i in range(1, N+1):
        for j in range(len(sub_set)):
            temp = sub_set[j]+[i]
            if len(temp) < N//2+0.5:
                sub_set.append(temp)
            if len(temp) == N//2:
                result.append(set(temp))

    return result

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*(N+1)]+[([0] + list(map(int, input().split()))) for _ in range(N)]
    sets = set(range(1, N+1))
    subsets = make_sets()
    min_value = int(1e9)

    subsets = make_sets()

    for subset in subsets:
        set1 = subset
        set2 = sets - subset
        temp = abs(calculate(list(set1))-calculate(list(set2)))
        if temp < min_value:
            min_value = temp
    print(f'#{tc} {min_value}')

