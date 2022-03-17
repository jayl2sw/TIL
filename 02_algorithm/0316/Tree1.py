import sys
sys.stdin = open('input.txt')

def pre_order(v):
    if v:
        print(v, end=" ")
        pre_order(ch1[v])
        pre_order(ch2[v])

def in_order(v, end=" "):
    if v:
        in_order(ch1[v])
        print(v, end=" ")
        in_order(ch2[v])

def post_order(v):
    if v:
        post_order(ch1[v])
        post_order(ch2[v])
        print(v)

E = int(input())
arr = list(map(int, input().split()))
V = E + 1

ch1 = [0] * (V+1)
ch2 = [0] * (V+1)
for i in range(E):
    p, o = arr[i*2], arr[i*2+1]
    if ch1[p] == 0:
        ch1[p] = o
    else:
        ch2[p] = o

pre_order(1)


