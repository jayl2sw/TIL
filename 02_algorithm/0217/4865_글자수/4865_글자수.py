import sys
sys.stdin = open('input.txt')

def mode_char(candidate, arr):
    max_count = 0
    for char in set(candidate):     # abc
        count = 0
        for ch in arr:          # asdbjadb
            if char == ch:
                count += 1
        if max_count < count:
            max_count = count
    return max_count




T = int(input())
for tc in range(1, T+1):
    candidates = input()
    arr = input()
    print(f'#{tc} {mode_char(candidates, arr)}')