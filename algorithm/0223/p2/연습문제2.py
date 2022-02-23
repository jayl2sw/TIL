def subset_10(k, N, s):
    if s == 10:
        for j in range(N):
            if bit[j]:
                print(arr[j], end=' ')
        print()
    elif k == N:
        return
    elif s > 10:
        return
    else:
        bit[k] = 1
        subset_10(k + 1, N, s + arr[k])
        bit[k] = 0
        subset_10(k + 1, N, s)


arr = [x for x in range(1, 11)]
bit = [0] * 11

subset_10(0, 10, 0)