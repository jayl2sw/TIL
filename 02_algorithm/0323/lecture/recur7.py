# A의 부분집합중 합이 K인 부분집합의 개수 구하기
def f(i, N, s):
    global cnt
    if s > K:
        return

    if i == N:
        if s == K:
            cnt += 1
    else:
        f(i + 1, N, s + A[i])
        f(i + 1, N, s)

A = [1,2,3,4,5,6,7,8,9,10]
N = len(A)
K = 22
cnt = 0
f(0, N, 0)
print(cnt)