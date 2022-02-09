def counting_sort(array, N):
    counts = [0] * (N+1)

    for i in range(len(array)):
        counts[array[i]] += 1

    for i in range(len(counts)-1):
        counts[i] += counts[i-1]


