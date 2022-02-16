import sys

sys.stdin = open('/input.txt')


def find_one1(array):
    for i in range(len(array)):
        if array[i] == 1:
            array[i] += array[i-1]

    return array


def find_one2(string):
    cnt = 0
    max_cnt = 0
    for num in string:
        if int(num):
            cnt += 1
            if max_cnt < cnt:
                max_cnt = cnt
        else:
            cnt = 0
    return max_cnt

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    array = list(map(int, input()))
    string = ''.join(map(str,array))
    print(f'#{tc} {max(find_one1(array))}')
    print(f'#{tc} {find_one2(string)}')
