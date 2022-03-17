import sys
sys.stdin = open("input.txt")

def pre(start):
    print(start, end=" ")
    for nxt in tree[start]:
        if nxt != 0:
            pre(nxt)


def mid(start):
    if tree[start][0] != 0:
        mid(tree[start][0])
    print(start, end=" ")
    if tree[start][1] != 0:
        mid(tree[start][1])


def post(start):
    for nxt in tree[start]:
        if nxt != 0:
            post(nxt)
    print(start, end=" ")

V = int(input())
E = V-1
arr = list(map(int, input().split()))
tree = [[0] * 3 for _ in range(V+1)]

for i in range(E):
    if tree[arr[i*2]][0] == 0:
        tree[arr[i * 2]][0] = (arr[i * 2 + 1])
    else:
        tree[arr[i * 2]][1] = (arr[i * 2 + 1])

print('='*30)
print('전위 순회')
pre(1)
print()
print('='*30)
print('중위 순회')
mid(1)
print()
print('='*30)
print('후위 순회')
post(1)
print()
print('='*30)