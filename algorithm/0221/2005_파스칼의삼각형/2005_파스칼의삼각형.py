pascal_tri = [None, [1],[1,1]]


def make_pascal_tri(n):
    for i in range(3, n+1):
        pascal_line = [1]
        for j in range(i-2):
            pascal_line.append(pascal_tri[i-1][j]+pascal_tri[i-1][j+1])
        pascal_line.append(1)
        pascal_tri.append(pascal_line)


make_pascal_tri(10)

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    print(f'#{tc}')
    for i in range(1, n+1):
        print(*pascal_tri[i])







