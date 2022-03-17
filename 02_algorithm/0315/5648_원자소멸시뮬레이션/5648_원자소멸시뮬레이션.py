import sys
sys.stdin = open('input.txt')


def come(x):
    r_direction = {'0':1, '1':0, '2':3, '3':2}
    return r_direction[str(x)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    atoms = [list(map(int, input().split())) for _ in range(N)]
    crash = []
    result = 0

    for i in range(2000):
        if not atoms:
            break
        for j in range(len(atoms)):
            atom = atoms[j]
            x, y, direction, K = atom
            nx = x + dx[direction]
            ny = y + dy[direction]
            for k in range(j + 1, len(atoms)):
                try:
                    r_atom = atoms[k]
                except:
                    break
                if atom == r_atom:
                    break
                r_x, r_y, r_direction, r_K = r_atom
                if direction == come(direction):
                    if r_x == x and (r_y + 1 == y or r_y - 1 == y):
                        crash.append(atom)
                        crash.append(r_atom)
                    elif r_y == y and (r_x + 1 == x or r_x - 1 == x):
                        crash.append(atom)
                        crash.append(r_atom)

            atom[0] = nx
            atom[1] = ny

        for j in range(len(atoms)):
            try:
                atom = atoms[j]
            except:
                break
            x, y, direction, K = atom
            for k in range(j+1, len(atoms)):
                r_atom = atoms[k]
                r_x, r_y, r_direction, r_K = r_atom
                if x == r_x and y == r_y:
                    if atom not in crash:
                        crash.append(atom)
                    crash.append(r_atom)

            for atom in crash:
                result += atom[3]
                atoms.remove(atom)
                crash =[]


    print(f'#{tc} {result}')