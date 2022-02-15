import sys
sys.stdin = open('sample_input.txt')

def subset(n, k):
    result = 0
    for i in range(1 << 12):
        count = 0
        total = 0
        for j in range(12):
            if i & (1 << j):
                count += 1
                total += j+1
        if count == n and total == k:
            result += 1
    return result


T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())
    print(f'#{tc} {subset(n, k)}')

