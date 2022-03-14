def snail(r, c, target):
    if target == 1:
        return 1, 1
    array = [[0] * r for _ in range(c)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    i = 2
    direction = 0
    x = 0
    y = 0
    array[0][0] = 1
    count = 1

    while count < int(r*c):
        nx = x + dx[direction]
        ny = y + dy[direction]

        if nx < 0 or ny < 0 or nx >= c or ny >= r or array[nx][ny]!= 0:
            direction += 1
            if direction == 4:
                direction = 0
            continue

        array[nx][ny] = i
        x = nx
        y = ny

        if i == target:
            return [x + 1, y + 1]

        i += 1
        count += 1

    return 0




c, r = map(int,input().split())
target = int(input())
result = snail(r, c, target)
if result == 0:
    print(0)
else:
    print(' '.join(map(str, result)))
