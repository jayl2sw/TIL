import sys
sys.stdin = open('input.txt')

def inorder_Traversal(start):
    if tree[start]:
        inorder_Traversal(tree[start].pop(0))
    print(words[start], end="")
    if tree[start]:
        inorder_Traversal(tree[start].pop(0))


for tc in range(1, 11):
    V = int(input())
    tree = [[] for _ in range(V+1)]
    words = [''] * (V+1)
    for i in range(V):
        idx, word, *next_nodes = input().split()
        idx = int(idx)
        words[idx] = word

        tree[idx].extend(map(int, next_nodes))


    print(f'#{tc}', end=' ')
    inorder_Traversal(1)
    print('')

