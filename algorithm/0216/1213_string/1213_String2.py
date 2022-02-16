import sys

sys.stdin = open('input.txt', encoding='utf-8')

def bf(pattern, target):
    result = target.count(pattern)
    return result


for tc in range(1, 11):
    n = int(input())
    pattern = input()
    target = input()
    print(f'#{n} {bf(pattern, target)}')





