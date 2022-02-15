import sys
sys.stdin = open('sample_input.txt')

def subset(n, k):
    result = 0
    for i in range(1 << 12):     # 2^12승까지 이진수로 나타냄
        count = 0                # 개수 초기화
        total = 0                # 총 합 초기화
        for j in range(12):      # 1 ~ 12까지 각 원소에 대해서
            if i & (1 << j):     # j번째 원소가 포함될 때,
                count += 1       # count += 1
                total += j+1     # total += j+1 j는 인덱스이므로 0~11이기 때문에 +1 해줌

            # 필요 없음
            if count > n:       # n개 넘어가면 안함
                break
            if total > k:       # 합이 k 넘어가면 안함
                break

        if count == n and total == k: # 개수가 n개이고 총 합이 k일 때, result 한개 추가
            result += 1
    return result


T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())
    print(f'#{tc} {subset(n, k)}')

