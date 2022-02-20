import sys
import time

sys.stdin = open('input.txt')
start = time.time()  # 시작 시간 저장


# n * n 행렬에서 m 길이의 팰린드롬 찾기
def palindrome(array, m):                                        # 아까 여러개로 이루어진 것을 하나로 만듬
    for row in array:  # 1 ~ 100
        for start in range(100 - m + 1):
            for i in range(m // 2):
                if row[start + i] != row[start + m - 1 - i]:
                    break
            else:
                return True
    return False

# ABA, BAAB가 없으면 CABAC와, CBAABC는 존재 할 수 없다.
def find_loggest_vertical(vertical):                                # 큰 거부터 줄여나가면서 찾음
    max_v = 1                                                       #
    for m in range(1, 100):                                         # 1부터 100까지
        if m > max_v + 2:                                           # 만약 max_v보다 2큰 회문이 존재하지 않는다면 그것보다 큰 회문 존재 x
            return max_v                                            # max_v 반환
        if palindrome(vertical, m):                                 # 만약 m 길이의 회문이 존재하면
            max_v = m                                               # max_v = m


def find_loggest_horizontal(horizontal, max_v):                 # Horizontal에서 큰거부터 하나하나 줄여나가면서 계산하면 시간이 너무 오래걸림
    max_h = max_v 
    for m in range(max_v, 100):                                 # max_v 보다 큰 것만 탐색
        if m > max_h + 2:                                       # 만약 max_h보다 2큰 회문이 존재하지 않는다면 그것보다 큰 회문 존재 x
            return max_h                                        # max_h 반환
        if palindrome(horizontal, m):                           # 만약 m 길이의 회문이 존재하면
            max_h = m                                           # max_h = m 할당


T = 10
for _ in range(1, T + 1):
    t = int(input())
    horizontal = [input() for _ in range(100)]
    vertical = list(zip(*horizontal))                           # 대칭 행렬 만들기 꿀팁

    max_v = find_loggest_vertical(vertical)
    max_h = find_loggest_horizontal(horizontal, max_v)

    result = max(max_v, max_h)
    print(f'#{t} {result}')

print("time :", time.time() - start)