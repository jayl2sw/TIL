import sys
sys.stdin = open('input.txt')

# 전체 테스트 케이스 개수
T = int(input())

# T만큼 반복해서 로직을 수행해서
# 3개의 tc에 대한 답안 각각 출력

for tc in range(1,T+1):
    N = int(input())
    numbers = list(map(int,input().split()))

    # 최종 결과값
    result = 0

    #모든 상황에 대한 낙찻값 구하기 위한 순회
    for i in range(N):
        # i번째의 최대 낙차값은
        # 전체 길이 - (내 현재 위치 + 1)
        max_height = len(numbers) - (i + 1)
        # i번째부터 끝까지 확인해서 더 큰 값 찾기
        for j in range(i+1, len(numbers)):
            # i 보다 큰 j 찾기
            if numbers[j] >= numbers[i]:
                max_height -= 1

        if result < max_height:
            result = max_height

    print(f'#{tc} {result}')

