def f(i, N, v):
    if i == N: # 배열을 벗어난 경우, 검색 실패
        return -1
    elif A[i] == v:
        return 1
    else:
        return f(i+1, N, v)

A = [7, 2, 5, 4, 1, 3]
N = len(A)
v = 5

print(f(0, N, v))