def f(i, N, v):
    if i == N: #A를 모두 채웠으면
        print(A)
    else:
        for j in range(1,6):
            A[i] = j
            f(i + 1, N)
    return

N = 3
A = [0] * N
f(0,N)
