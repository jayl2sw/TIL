def switch(x):
    if x == '1':
        return '0'
    else:
        return '1'


def bchanges(b):
    result = []
    for i in range(len(b)):
        result.append(b[:i] + switch(b[i]) + b[i+1:])

    return result

def tchanges(t):
    result = []
    for i in range(len(t)):
        if t[i] == '0':
            result.append(t[:i] + '1' + t[i+1:])
            result.append(t[:i] + '2' + t[i + 1:])
        elif t[i] == '1':
            result.append(t[:i] + '0' + t[i+1:])
            result.append(t[:i] + '2' + t[i + 1:])
        else:
            result.append(t[:i] + '0' + t[i + 1:])
            result.append(t[:i] + '1' + t[i + 1:])
    return result

def btoDecimal(b):
    result = 0
    for i in range(len(b) - 1, -1, -1):
        result += int(b[i]) * 2 ** int(len(b) - 1 - i)
    return result

def ttoDecimal(t):
    result = 0
    for i in range(len(t) - 1, -1, -1):
        result += int(t[i]) * 3 ** int(len(t) - 1 - i)
    return result


T = int(input())
for tc in range(1, T+1):
    binary = input()
    ternary = input()
    b = btoDecimal(binary)
    t = ttoDecimal(ternary)
    bv = []
    tv = []
    for x in bchanges(binary):
        bv.append(btoDecimal(x))
    for y in tchanges(ternary):
        tv.append(ttoDecimal(y))

    for i in set(bv)&set(tv): print(f'#{tc} {i}')