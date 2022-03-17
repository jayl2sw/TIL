import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, B = map(int, input().split())
    clerks = list(map(int, input().split()))
    clerks.sort()
    d = [0]
    min_v = int(1e9)
    for clerk in clerks:
        for i in range(len(d)):
            tmp = d[i] + clerk
            if tmp >= B and min_v > tmp:
                min_v = tmp
            if tmp <= min_v:
                d.append(d[i]+clerk)
    print(f'#{tc} {min_v-B}')

    # clerks.sort(reverse=True)

    # total = 0
    # idx = 0
    # min_v = int(1e9)

    # while clerks[idx] > B:
    #     min_v = clerks[idx]
    #     idx += 1
    #
    # while total < B:
    #     total += clerks[idx]
    #     last = clerks[idx]
    #     idx += 1
    #
    # total = total - last
    # print(total, B)
    # idx = 1
    # temp = -1
    # while temp < 0:
    #     temp = total + clerks[-idx] - B
    #     print(clerks[idx])
    #     idx += 1
    #
    #
    # print(f'#{tc} {min(temp, min_v-B)}')
