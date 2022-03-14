import sys
sys.stdin = open('input.txt')

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


# 대칭 행렬 만들기
def reverse_array(n, array):
    for i in range(n):
        for j in range(n):
            if i < j:                                                  # i가 j보다 작으면
                array[i][j], array[j][i] = array[j][i], array[i][j]    # array[i][j] 와 array[j][i] 바꿈


# n * n 행렬에서 m 길이의 팰린드롬 찾기
def find_palindrome(n, m, array):
    for i in range(2):                                  # 가로, 세로 탐색
        for i in range(n):                              # 0부터 n번 째 행까지
            result = find_palindrome_line(m, array[i])  # i번째 행에서 m 길이의 회문 탐색해서 변수에 저장
            if result:                                  # 만약 회문이라면 result = 해당 회문, 회문이 아니라면 result = None
                return result                           # result가 회문일 때, 해당 회문 반환

        reverse_array(n,array)




T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(input()) for i in range(n)]
    print(f'#{tc} {"".join(find_palindrome(n, m, arr))}')
