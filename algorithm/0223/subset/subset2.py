def powerset(i, N, s, t, result):
    temp = []
    if s == t:
        for j in range(N):
            if bit[j]:
                temp.append(arr[j])
        result.append(temp)
    elif i == N:
        return
    elif s > t:
        return
    else:
        bit[i] = 1
        powerset(i + 1, N, s + arr[i], t, result)
        bit[i] = 0
        powerset(i + 1, N, s, t, result)
    return


def subset(N, target):
    result = []
    powerset(0, N, 0, target, result)
    return result


N = 10
arr = [x for x in range(1, N + 1)]
bit = [0] * N
target = 10

print(subset(N, target))
