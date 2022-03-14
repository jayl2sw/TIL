# kmp

# Pre-Processing
def make_lps(p):
    m = len(p)
    lps = [0] * (m + 1)
    j = 0  # 일치한 개수 == 비교할 패턴 위치
    lps[0] = -1
    for i in range(1, m):
        lps[i] = j  # p[i] 이전에 일치한 개수
        if p[i] == p[j]:
            j += 1
        else:
            j = 0
    lps[m] = j

    return lps


def kmp(t, p):
    n = len(t)
    m = len(p)
    lps = make_lps(p)

    # Search
    i = 0
    j = 0
    while i < n and j <= m:
        if j == -1 or t[i] == p[j]:
            i += 1
            j += 1
        else:
            j = lps[j]
        if j == m:
            print(i-m, end=' ')
            j = lps[j]

kmp('asasdsasdasd','asdasd')