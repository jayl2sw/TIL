import sys
sys.stdin = open('input.txt')


def check(i, j):
    if 0 <= i < N and 0 <= j < N:
        return True
    return False

def house(i, j):
    k = 1
    inside = 1 if arr[i][j] == 1 else 0
    while inside * M >= k ** 2 + (k-1) ** 2:
        for di in range(k):
            dj = k - di - 1
            if di != 0 or dj != 0:
                if check(i + di, j + dj) and arr[i + di][j + dj] == 1:
                    inside += 1
                if check(i + di, j - dj) and arr[i + di][j - dj] == 1:
                    inside += 1
                if check(i - di, j + dj) and arr[i - di][j + dj] == 1:
                    inside += 1
                if check(i - di, j - dj) and arr[i - di][j - dj] == 1:
                    inside += 1
            else:
                if check(i + di, j + dj) and arr[i + di][j + dj] == 1:
                    inside += (1/2)
                if check(i + di, j - dj) and arr[i + di][j - dj] == 1:
                    inside += (1/2)
                if check(i - di, j + dj) and arr[i - di][j + dj] == 1:
                    inside += (1/2)
                if check(i - di, j - dj) and arr[i - di][j - dj] == 1:
                    inside += (1/2)
        k += 1

    return inside


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    x = [0, 0]
    for i in range(N):
        for j in range(N):
            y = house(i,j)
            if y > result:
                x = [i, j]
                result = y

    print(x, result)
