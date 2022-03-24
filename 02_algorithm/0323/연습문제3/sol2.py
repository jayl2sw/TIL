pattern = ['001101', '010011', '111011', '110001', '100011', '110111', '001011', '111101', '011001', '101111']

import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(T):
    array = input()
    arr = ''
    for i in range(len(array)):
        arr += bin(int(array[i], 16)).replace('0b', '').zfill(4)

    for i in range(len(arr)):
        if arr[i:i+6] in pattern:
            start = i
            break

    arr = arr[start:]
    while arr:
        now = arr[:6]
        arr = arr[6:]
        if now in pattern:
            print(pattern.index(now), end=' ')
        else:
            continue

    print()
