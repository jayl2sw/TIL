import sys
sys.stdin = open('input.txt')

password = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9
}


def getResult(passwords):               # 구한 password 들 중 옳은 것 다 더하기
    result = 0
    for p in passwords:
        even = 0
        odd = 0
        for pi in range(8):
            if pi % 2:
                even += int(p[pi])      # 짝수 더하고
            else:
                odd += int(p[pi])       # 홀수 더해서

        if (odd * 3 + even) % 10 == 0:  # 조건 확인
            result += (odd + even)        # 조건 맞으면 result에 더함

    return result


def findI(b_line):
    i = 1
    while True:
        for j in range(8):
            if b_line[len(b_line) - 7 * (j + 1) * i:len(b_line) - 7 * j * i:i] not in password:   # 만약 끝까지 다 들어가면
                i += 1                                                                            # i를 1부터 1씩 키우면서
                break

        if j == 7:
            return i                                                                              # 해당 i 반환


def findPassword(tmp):                         # 56자리 2진수로 비밀번호 8자리 만듬
    pw = ''
    while tmp:
        now = tmp[:7]
        tmp = tmp[7:]
        if now in password:
            pw += str(password[now])
        else:
            break

    return pw


T = int(input())

for tc in range(1, T+1):
    passwords = set()                                                                   # 찾은 패스워드를 넣을 set
    N, M = map(int, input().split())                                                    # N, M
    arr = list(set(input().strip('0') for _ in range(N)))                               # input.txt 받음
    # arr = list(set(input.txt().strip().strip('0') for _ in range(N)))

    for line in arr:
        if line:                                                                        # 0만 있는 곳이 아닐 때,
            b_line = ''
            for k in range(len(line)):
                b_line += bin(int(line[k], base=16)).replace('0b', '').zfill(4)         # 2진수로 나타냄

            b_line = b_line.rstrip('0')                                    # 뒤에 있는 0 떼고 앞에는 원래 길이만큼 더해줌

            while b_line:                                                               # 2진수로 나타낸 라인을 돌면서
                i = findI(b_line)                                                       # i 찾기 (몇배인지)
                tmp = b_line[len(b_line) - 56 * i:len(b_line):i]                        # 뒤에서부터 이번에 탐색할 만큼 떼어냄

                b_line = b_line[:len(b_line) - 56 * i]                                  # 나머지를 b_line으로 둔다

                pw = findPassword(tmp)                                                  # tmp 넣어서 pw 찾음

                # if len(pw) == 8:                                                       # 만약 password가 길이가 8이라면
                passwords.add(pw)

                b_line = b_line.rstrip('0')                                             # 1로 끝날때까지 0 제거

    result = getResult(passwords)

    print(f'#{tc} {result}')


