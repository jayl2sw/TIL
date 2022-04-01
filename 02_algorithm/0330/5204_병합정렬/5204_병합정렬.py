import sys
sys.stdin = open("input.txt")
def merge_sort(arr):
    global cnt
    if len(arr) <= 1:
        return arr

    front = arr[:len(arr)//2]
    end = arr[len(arr)//2:]

    arr1 = merge_sort(front)
    arr2 = merge_sort(end)

    if arr1[-1] > arr2[-1]:
        cnt += 1

    result = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i+=1
        else:
            result.append(arr2[j])
            j+=1

    if i == len(arr1):
        result += arr2[j:]
    else:
        result += arr1[i:]

    return result



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    cnt = 0
    print(f'#{tc} {merge_sort(arr)[N//2]} {cnt}')
