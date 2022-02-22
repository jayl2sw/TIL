import sys
sys.stdin = open('input.txt')

def paper(n):
    d = [0]* 31
    d[1] = 1
    d[2] = 3

    for i in range(3, n+1):
        d[i] = d[i-1] + 2 * d[i-2]
    return d[n]

T = int(input())
for tc in range(1, T+1):
    n = int(input())//10
    print(f'#{tc} {paper(n)}')


