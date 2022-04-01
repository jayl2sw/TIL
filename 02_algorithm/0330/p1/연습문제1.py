import sys
sys.stdin = open('input.txt')

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    tail = arr[1:]
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


T = int(input())
for tc in range(1, T+1):
    arr = list(map(int,input().split()))
    print(f'#{tc} {" ".join(map(str, quick_sort(arr)))}')
