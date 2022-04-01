import sys
sys.stdin = open('input.txt')


def queue(arr, n):
    oven = arr[:n]
    rest = arr[n:]
    while len(oven) > 1:

        temp = oven.pop(0)
        if temp[1]//2:
            oven.append([temp[0], temp[1]//2])
        else:
            if rest:
                oven.append(rest.pop(0))

    return oven[0][0]


T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = list(enumerate(list(map(int, input().split())), start=1))
    # list(enumerate(list(map(int, input.txt().split())), start=1))
    # [[i, v] for i, v in enumerate(list(map(int, input.txt().split())), start=1)]
    # print(arr)
    result = queue(arr, n)
    print(f'#{tc} {result}')

