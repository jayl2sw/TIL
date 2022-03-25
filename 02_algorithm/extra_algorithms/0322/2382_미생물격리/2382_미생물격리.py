import sys
sys.stdin = open('input.txt')

opp = [0, 2, 1, 4, 3]
T = int(input())

di = [0, -1, 1, 0, 0]
dj = [0, 0, 0, -1, 1]

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(K)]

    for _ in range(M):
        for i in range(len(arr)):
            arr[i][0] += di[arr[i][3]]
            arr[i][1] += dj[arr[i][3]]
            if arr[i][0] == 0 or arr[i][0] == N-1 or arr[i][1] == 0 and arr[i][1] == N-1:
                arr[i][3] = opp[arr[i][3]]
                arr[i][2] = arr[i][2]//2

        arr = sorted(arr, key=lambda x: (x[0], x[1], x[2]), reverse=True)

        j = 1
        while j < len(arr):
            if arr[j][0] == arr[j-1][0] and arr[j][1] == arr[j-1][1]:
                arr[j-1][0] += arr[j][0]
                arr.pop(j)
            else:
                j += 1

    result = 0
    for m in arr:
        print(m)

    print(f'#{tc} {result}')





