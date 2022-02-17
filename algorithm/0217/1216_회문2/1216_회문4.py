import sys
sys.stdin = open('input.txt')

# n * n 행렬에서 m 길이의 팰린드롬 찾기
def palindrome(array, m):
    for row in array:  # 1 ~ 100
        for start in range(100 - m + 1):
            for i in range(m // 2):
                if row[start + i] != row[start + m - 1 - i]:
                    break
            else:
                return True
    return False

def find_loggest(vertical, horizontal):
    maxLength = 1
    for m in range(2, 101):
        if m > maxLength + 2:  # 기존보다 길이가 2개이상 큰 회문이 없다면 그보다 큰 회문이 없으므로 그만한다.
            break
        if palindrome(vertical, m):  # 만약
            maxLength = m

    for m in range(maxLength + 1, 101):
        if m > maxLength + 2:
            break
        if palindrome(horizontal, m):
            maxLength = m
    return maxLength

T = 10
for _ in range(1, T + 1):
    t = int(input())
    vertical = [input() for _ in range(100)]
    horizontal = list(zip(*vertical))

    result = find_loggest(vertical, horizontal)
    print(f'#{t} {result}')
