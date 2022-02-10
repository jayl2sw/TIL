import sys

sys.stdin = open('sample_input.txt')


def max(set):
    max_val = -int(1e9)
    for i in set:
        if max_val < i:
            max_val = i
    return max_val


def stop_times(n, k, array): #n, k, array = 충전기 위치 idx
    location = 0    # 현재 위치
    count = 0       # 충전 횟수
    while True:
        if location + k >= n:   # 목적지에 도착하면 count 반환
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
