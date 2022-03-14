import sys
sys.stdin = open('sample_input.txt')


def paint(array):
    x1, y1, x2, y2, color = array
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            paper[i][j] += color


def find_purple():
    count = 0
    for x in range(10):
        for y in range(10):
            if paper[x][y] == 3:
                count += 1
    return count


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    paper = [[0] * 10 for _ in range(10)]           # 빈종이 생성

    for k in range(n):                              # n번
        array = list(map(int, input().split()))     # 영역, 색상 받아서
        paint(array)                                # 색칠

    result = find_purple()                          # 전체 종이에서 보라색 요소 개수 찾기

    print(f'#{tc} {result}')