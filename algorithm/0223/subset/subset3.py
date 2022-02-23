def powerset(i, N, s, t, rs):
    if s == t:
        for j in range(N):
            if bit[j]:
                print(arr[j], end=' ')
        print()
    elif i == N:
        return
    elif s > t:
        return
    elif s + rs < t:
        return
    else:
        bit[i]= 1
        powerset(i + 1, N, s + arr[i], t, rs - arr[i])
        bit[i] = 0
        powerset(i + 1, N, s , t, rs - arr[i])
    return



N = 10
arr = [x for x in range(1, N+1)]
bit = [0] * N
t = 10
powerset(0, N, 0, t, sum(arr))