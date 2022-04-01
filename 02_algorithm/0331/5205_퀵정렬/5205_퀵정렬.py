import sys
sys.stdin = open('input.txt')

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]

    left = []
    mid = []
    right = []
    for a in arr:
        if a > pivot:
            right.append(a)
        elif a < pivot:
            left.append(a)
        else:
            mid.append(a)
    #
    # left = [x for x in arr if x < pivot]
    # right = [x for x in arr if x >= pivot]
    return quick_sort(left) + mid + quick_sort(right)



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    print(quick_sort(arr))
    print(f'#{tc} {quick_sort(arr)[N//2]}')
