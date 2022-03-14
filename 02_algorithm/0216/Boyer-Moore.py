def makeSkip(pattern):
    num = 27
    m = len(pattern)
    skip = [m for i in range(num)]
    for i in range(m):
        skip[ord(pattern[i]) - ord('a')] = m - i - 1
    return skip

def boyer_moore(text, pattern):
    n = len(text)
    m = len(pattern)
    skip = makeSkip(pattern)

    i = m - 1
    j = m - 1

    while j >= 0:
        while text[i] != pattern[j]:
            k = skip[ord(text[i]) - ord('a')]
            if m -j > k:
                i = i + m - j
            else:
                i = i + k
            if i >= n:
                return n
            j = m - 1
        i -= 1
        j -= 1
    return i + 1

print(boyer_moore('httpseiosaheiasosaoehsaositesehoashr', 'sites'))