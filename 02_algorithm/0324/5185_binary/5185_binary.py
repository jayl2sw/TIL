import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N, arr = input().split()
    result = ''
    for i in range(int(N)):
        result += bin(int(arr[i], base=16)).replace('0b','').zfill(4)

    print(f'#{tc} {result}')