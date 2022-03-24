import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    array = input()
    arr = ''
    for i in range(len(array)):
        arr += bin(int(array[i], 16)).replace('0b', '').zfill(4)
        print(arr)


    while arr:
        now = arr[:7]
        arr = arr[7:]

        result = 0
        for i in range(len(now)):
            result = result * 2 + int(now[i])
        print(result, end=' ')
    print()






