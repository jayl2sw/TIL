import sys
sys.stdin = open('input.txt')

def mode_char(candidate, arr):
    result = 0
    for char in candidate:
        count = 0
        for ch in arr:
            if char == ch:
                count += 1
        if result < count:
            result = count
    return result




T = int(input())
for tc in range(1, T+1):
    candidates = input()
    arr = input()
    print(f'#{tc} {mode_char(candidates, arr)}')