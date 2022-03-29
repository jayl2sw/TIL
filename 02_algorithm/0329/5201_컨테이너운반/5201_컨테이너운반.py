import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    weights = sorted(list(map(int, input().split())), reverse=True)
    capacities = sorted(list(map(int, input().split())), reverse=True)

    idx = 0
    total = 0
    for i in range(len(capacities)):
        # 해당 capacity에 넣을 수 있는 weight을 찾을 수 있을 때 까지 idx 증가
        while i + idx < len(weights) and capacities[i] < weights[i+idx]:
            idx += 1
        if i + idx < len(weights):
            total += weights[i + idx]

    print(f'#{tc} {total}')


