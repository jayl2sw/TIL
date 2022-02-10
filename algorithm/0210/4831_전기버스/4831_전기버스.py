import sys

sys.stdin = open('sample_input.txt')


def stop_times(n, k, array):
    location = 0
    count = 0
    while True:
        if location + k >= n:
            return count
        mid_charger = set(range(location + k, location, -1)) & set(array)
        if mid_charger:
            location = max(mid_charger)
            count += 1
            continue

        return 0



T = int(input())

for tc in range(1, T + 1):
    k, n, m = map(int, input().split())
    array = list(map(int, input().split()))
    print(f'#{tc} {stop_times(n, k, array)}')
