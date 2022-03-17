import sys
sys.stdin = open("input.txt")

def make_tree(start):
    global idx
    if start > N:
        return None
    make_tree(start*2)
    tree[start] = idx
    idx += 1
    make_tree(start * 2 + 1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = list(range(N+1))
    idx = 1
    make_tree(1)
    print(tree)
    print(f'#{tc} {tree[1]} {tree[N//2]}')




