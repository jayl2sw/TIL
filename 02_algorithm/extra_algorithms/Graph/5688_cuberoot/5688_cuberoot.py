T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cube_root = round(N**(1/3), 5)
    if cube_root % 1 == 0:
        result = cube_root
    else:
        result = -1
    print(f'#{tc} {int(result)}')
