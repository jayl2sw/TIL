import sys
sys.stdin = open('input.txt')

def itoa1(i):
    result = ''
    num = abs(i)
    array = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    while num > 0:
        last = num % 10
        result = array[last] + result
        num //= 10
    if i < 0:
        result = '-' + result
    return result


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    a = itoa1(n)
    print(f'#{tc} {a} {type(a)}')