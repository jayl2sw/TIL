def perm(i, N, r):
    if i == N:
        print(p[:r])
    else:
        for j in range(1, N):
            p[i],p[j] = p[j],p[i]
            perm(i+1, N, r)
            p[i], p[j] = p[j], p[i]

N = 4
p = [x for x in range(1, N+1)]
result = []
perm(0, N, 2)