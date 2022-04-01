# import sys
# sys.stdin = open('input.txt.txt')
password = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9
}

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = set(input() for _ in range(N))
    arr = arr.pop().strip('0')


    even = 0
    odd = 0
    preprocessed_line = ''
    for k in range(len(arr)):
        preprocessed_line += bin(int(arr[k], base=16)).replace('0b', '').zfill(4)

    arr = preprocessed_line.rstrip('0')
    now = arr[len(arr)-7:]
    arr = arr[:len(arr)-7]

    idx = 7
    print(now)
    print(arr)
    while now in password:
        print(password[str(now)])
        if idx % 2:
            even += password[str(now)]
        else:
            odd += password[str(now)]

        now = arr[len(arr) - 7:]
        arr = arr[:len(arr) - 7]
        idx -= 1

    if (odd * 3 + even) % 10 == 0:
        result = odd + even
    else:
        result = 0

    print(f'#{tc} {result}')


