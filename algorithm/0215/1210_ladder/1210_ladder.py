import sys
sys.stdin = open('input.txt')

# 2를 찾는다.
def find_destination(array):
    for i in range(len(array[-1])):
        if array[-1][i] == 2:
            return i

# 2에서 위로 올라간다

# 올라갈때마다 좌우를 살피고
# 만약 좌우로 움직일 수 있으면 좌우로 움직인다.

# 좌우로 움직이다가 다시 위로 갈 수 있을 때, 위로 간다.

def ladder(array):
    x = len(array) - 1
    y = find_destination(array)
    direction = 2

    dx = [0, 0, -1]
    dy = [1, -1, 0]

    while True:
        if x == 0:
            return y

        if direction == 2:
            for i in range(3):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= 100 or ny >= 100:
                    continue

                if array[nx][ny] == 1:
                    x = nx
                    y = ny
                    direction = i
                    break

        else:
            nx = x + dx[direction]
            ny = y + dy[direction]

            if nx < 0 or ny < 0 or nx >= 100 or ny >= 100 or array[nx][ny] == 0:
                direction = 2
                x = x - 1
                y = y

            else:
                x = nx
                y = ny

for tc in range(1, 11):
    n = int(input())
    array = [list(map(int,input().split())) for _ in range(100)]
    print(f'#{n} {ladder(array)}')