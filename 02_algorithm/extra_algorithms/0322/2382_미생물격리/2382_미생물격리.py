import sys
sys.stdin = open('input.txt')

di = [0, -1, 1, 0, 0]
dj = [0, 0, 0, -1, 1]
opp = [0, 2, 1, 4, 3]
T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(K)]

    # 0. M 이라는 시간 동안,
    for _ in range(M):
        # 1-1. 모든 미생물 군집 이동
        for i in range(len(arr)):
            arr[i][0] = arr[i][0] + di[arr[i][3]]
            arr[i][1] = arr[i][1] + dj[arr[i][3]]
            # 1-2. 만약 미생물이 가에 다달았다면, 뒤돌고 절반
            if arr[i][0] <= 0 or arr[i][0] >= N-1 or arr[i][1] <= 0 or arr[i][1] >= N-1:
                arr[i][3] = opp[arr[i][3]]
                arr[i][2] = arr[i][2] // 2

        # 2. 위치와 미생물 군집의 내림차순으로 arr 정렬
        arr = sorted(arr, key=lambda x: (x[0],x[1],x[2]), reverse=True)

        # 3. 위에서부터 돌면서 위치가 같으면 미생물수 더하고 밑에열 삭제
        j = 1
        while j < len(arr):
            if arr[j][0] == arr[j-1][0] and arr[j][1] == arr[j-1][1]:
                arr[j-1][2] += arr[j][2]
                arr.pop(j)

            else:
                j += 1

    result = 0
    for m in arr:
        result += m[2]

    print(f'#{tc} {result}')

