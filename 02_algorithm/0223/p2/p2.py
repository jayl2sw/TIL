arr = list(range(1, 11))
print(arr)

N = len(arr)

def powerset(arr, idx, temp, total):
    global cnt
    cnt += 1
    if sum(temp) > total:
        return
    if idx == N:
        if sum(temp) == total:
            print(temp)
        return


    powerset(arr, idx + 1, temp + [arr[idx]], total)
    powerset(arr, idx + 1, temp, total)

cnt = 0
powerset(arr, 0, [], 15)
print(cnt)