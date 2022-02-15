import sys
sys.stdin = open('sample_input.txt')


def paint(array):
    x1, y1, x2, y2, color = array
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            paper[i][j] += color

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    paper = [[0] * 10 for _ in range(10)]
    for k in range(n):
        array = list(map(int,input().split()))
        paint(array)

    count = 0
    for x in range(10):
        for y in range(10):
            if paper[x][y] == 3:
                count += 1

    print(f'#{tc} {count}')