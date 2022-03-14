import sys
import time

sys.stdin = open('input.txt')
start = time.time()  # 시작 시간 저장

# 회문인지 판단
def palindrome(string):
    l = len(string)                         # l
    for i in range(l // 2):                 # 처음부터 중간까지
        if string[i] != string[l - 1 - i]:  # 앞에서 i번째와 뒤에서 i번째가 다르면
            return False                    # False
    return True                             # 처음부터 중간까지 모두 같다면 True


# 한 줄에서 m 길이의 회문 찾기
def find_palindrome_line(m, string):        # input으로 주어진 회문의 길이: m, 탐색할 문자열: string
    for i in range(len(string) - m + 1):    # 0 ~ string의 길이 - m - 1 // m + i가 스트링을 벗어나지 않도록!
        check = string[i:i + m]             # slicing 통해서 체크할 string을 변수에 담고
        if palindrome(check):               # 회문인지 확인하고 만약 회문이면
            return check                    # 해당 문자열 반환


# 대칭 행렬 만들기                              ==> 시간 너무 오래 걸린다!
def reverse_array(n, array):
    for i in range(n):
        for j in range(n):
            if i < j:                                                  # i가 j보다 작으면
                array[i][j], array[j][i] = array[j][i], array[i][j]    # array[i][j] 와 array[j][i] 바꿈


# n * n 행렬에서 m 길이의 팰린드롬 찾기
# 가로 세로 한번에 하는 방법 찾아보기!
def find_palindrome(n, m, array):
    for i in range(2):                                  # 가로, 세로 탐색
        for i in range(n):                              # n번 째 행까지
            result = find_palindrome_line(m, array[i])  # i번째 행에서 m 길이의 회문 탐색해서 변수에 저장
            if result:                                  # 만약 회문이라면 result = 해당 회문, 회문이 아니라면 result = None
                return result                           # result가 회문일 때, 해당 회문 반환
        reverse_array(n, array)                          # 대칭행렬로 만들어 세로를 가로로 만듬


# 행렬에서 가장 긴 회문 찾기
def find_longest_palindrome(array):
    for i in range(100, 0, -1):                         # 찾는 회문의 길이를 100부터 1까지 1씩 줄여가면서
        result = find_palindrome(100, i, array)         # 100 * 100 행렬에서 i길이의 회문 찾음
        if result:                                      # 회문 찾은 즉시
            return i                                    # 회문 반환



for tc in range(1, 11):
    n = int(input())
    array = [list(input()) for i in range(100)]         # String으로 받으면 x, y 바꾸지 못한다.
    print(f'#{tc} {find_longest_palindrome(array)}')

print("time :", time.time() - start)