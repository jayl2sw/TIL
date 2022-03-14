def counting_sort(array, N):
    counters = [0] * (N+1)
    temp = [0] * N
    for number in array:
        counters[number] += 1

    for i in range(1, len(counters)):
        counters[i] += counters[i-1]

    for i in range(N-1, -1, -1):
        temp[counters[array[i]]-1] = array[i]
        counters[array[i]] -= 1

    return temp

numbers = [1,5,3,2,4,1,1,4,5,3]
print(counting_sort(numbers, 10))
