def bubble_sort(array, N):
    for i in range(N, -1, -1):
        for j in range(i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    return array

N = int(input())
array = list(map(int, input().split()))

print(bubble_sort(array, N))

