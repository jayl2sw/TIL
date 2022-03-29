import sys
sys.stdin = open('input.txt')
T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     # 종료 지점을 우선으로 정렬 진행
#     # ex) 4-8과 3-9 중에는 전자가 더 좋기 때문에
#     arr = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: (x[1], x[0]))
#     dock = [arr[0]]
#
#     for freight in arr:
#         if freight[0] >= dock[-1][1]:
#             dock.append(freight)
#             continue
#
#     print(f'#{tc} {len(dock)}')



for tc in range(1, T+1):
    N = int(input())
    # 종료 지점을 우선으로 정렬 진행
    # ex) 4-8과 3-9, 4-9, 5-9 중에는 전자가 더 좋기 때문에
    arr = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: (x[1], x[0]))
    result = 1
    last = arr[0][1]

    for freight in arr:
        if freight[0] >= last:
            last = freight[1]
            result += 1


    print(f'#{tc} {result}')