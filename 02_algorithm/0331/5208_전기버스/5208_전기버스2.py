def solution(array, destination):
    start = 0
    distance = array[start]
    cnt = 0
    while start + distance < destination:
        tmp = 0
        for i in range(start+1, start + distance+1):
            if tmp < i + array[i]:
                tmp = i + array[i]
                start = i
                distance = array[i]

        cnt += 1

    return cnt

T = int(input())
for tc in range(1, T+1):
    N, *arr = list(map(int,input().split()))
    print(solution(arr, N-1))
