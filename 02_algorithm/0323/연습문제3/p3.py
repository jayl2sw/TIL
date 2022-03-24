import sys
sys.stdin = open("input.txt")


def findpattern(pattern, arr):
    N = len(arr)
    for i in range(N-1, -1, -1):
        if arr[i] == '1':
            if arr[i-5:i+1] in pattern:
                end = i
                break

    k = (end+1) // 6
    start = end - k * 6 + 1

    return start, end+1


pattern = ['001101', '010011', '111011', '110001', '100011', '110111', '001011', '111101', '011001', '101111']

T = int(input())
for tc in range(T):
    array = input()
    arr = ''
    for i in range(len(array)):
        arr += bin(int(array[i], 16)).replace('0b', '').zfill(4)

    start, end = findpattern(pattern, arr)
    arr = arr[start: end]
    while arr:
        now = arr[:6]
        arr = arr[6:]
        if now in pattern:
            print(pattern.index(now), end=' ')
        else:
            continue
            
    print()



