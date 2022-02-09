def Bubble_Sort(array, N): # 정렬할 리스트, 원소의 수
    for i in range(N-1, 0, -1):
        for j in range(i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    return array

numbers = [1,8,6,7,2]
print(Bubble_Sort(numbers, 5))