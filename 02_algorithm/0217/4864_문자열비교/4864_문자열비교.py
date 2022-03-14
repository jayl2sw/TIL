import sys
sys.stdin = open('input.txt')

def make_skip(pattern):
    num = 26                                                # 알파벳이 26자라서 26
    m = len(pattern)                                        # 패턴의 길이를 m으로 둡니다.
    skip = [m for i in range(num)]                          # 스킵 리스트를 만듭니다. ex) [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
    for i in range(m):                                      # 패턴의 길이만큼 순회
        skip[ord(pattern[i]) - ord('A')] = m - i - 1        # 스킵[0]이 A 스킵[1]이 B 쭉해서 m-i-1
                                                            # ex) [4, 1, 4, 4, 3, 4, 4, 4, 4, 2, 4]
    print(skip)                                                            # 글자 위치만큼 빼줍니다.
    return skip                                             # 이게 해당 패턴의 스킵 어레이가 됨 kmp에서 lps느낌

def boyer_moore(pattern, text):
    n = len(text)                                           # 패턴 길이, 텍스트 길이
    m = len(pattern)
    skip = make_skip(pattern)                               # 패턴의 스킵 어레이 생성

    i = m - 1                                               # 뒤에서부터 확인할거니까 처음 확인하는 문자열의 제일 마지막 인덱스
    j = m - 1                                               # j가 pattern내에서 확인하는 인덱스

    while j >= 0:                                           # j가 0일 때, text내에서 패턴을 찾음
        while text[i] != pattern[j]:                        # 이건 틀렸을 때,
            k = skip[ord(text[i]) - ord('A')]               # 해당 알파벳의 skip값을 k에 넣음
            if m - j > k:                                   # 만약 m - j > k 이면 지금까지 검사한 것 중에 skip값이 m이 아닌게 있다.
                i = i + m - j                               # 그곳으로 돌아감
            else:
                i = i + k                                   # 탐색한 구간에 돌아갈 곳이 없으면 그대로 pattern의 길이만큼 스킵
            if i >= n:
                return 0                                    # 만약 index i 가 n에 도달하면 패턴이 존재하지 않음으로 return 0
            j = m - 1
        i -= 1                                              # 맞을 때, i 한칸 뒤로
        j -= 1                                              #         j 한칸 뒤로
    return 1                                                # j가 0보다 작아지면 모든 글자가 일치하므로 return 1

T = int(input())
for tc in range(1, T+1):
    pattern = input()
    text = input()
    result = boyer_moore(pattern, text)
    print(f'#{tc} {result}')