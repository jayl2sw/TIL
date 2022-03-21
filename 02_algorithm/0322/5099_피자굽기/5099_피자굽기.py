import sys
sys.stdin = open('input.txt')

T = int(input())

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


for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [[i, v] for i, v in enumerate(list(map(int, input().split())), start=1)]
    result = queue(arr, n)
    print(f'#{tc} {result}')

