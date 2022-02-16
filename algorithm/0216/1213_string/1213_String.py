import sys

sys.stdin = open('input.txt', encoding='utf-8')

def bf(pattern, target):
    count = 0
    for i in range(0, len(target)-len(pattern)+1):
        sub = 0
        for j in range(len(pattern)):
            if pattern[j] != target[i+j]:
                break
            sub += 1
        if sub == len(pattern):
            count += 1
    return count


for tc in range(1, 11):
    n = int(input())
    pattern = input()
    target = input()
    print(f'#{n} {bf(pattern, target)}')





