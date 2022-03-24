T = int(input())
for tc in range(1, T+1):
    N = float(input())
    result = ''
    for i in range(12):
        if N:
            if N * 2 >= 1:
                result += '1'
                N = N * 2 -1
            else:
                result += '0'
                N *= 2
    if N:
        result = 'overflow'

    print(f'#{tc} {result}')


