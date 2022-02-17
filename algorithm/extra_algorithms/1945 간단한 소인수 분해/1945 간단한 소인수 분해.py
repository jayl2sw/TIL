import sys
sys.stdin = open("input.txt")

def divide(n):
    arr = [2, 3, 5, 7, 11]
    result = []
    for number in arr:
        count = 0
        while n % number == 0:
            n /= number
            count += 1
        result.append(count)
    return result

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    print(f'#{tc} {" ".join(map(str, divide(n)))}')


