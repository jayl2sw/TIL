def enq(n):
    global last
    last += 1
    tree[last] = n
    c = last
    p = c//2
    while p >= 1 and tree[p] < tree[c]:
        tree[p], tree[c] = tree[c], tree[p]
        c = p
        p = c//2


def deq():
    global last
    tmp = tree[1]
    tree[1] = tree[last]
    last -=1
    p = 1
    c = p * 2
    while c <= last:
        if c+1 <= last and tree[c] < tree[c+1]:
            c = c + 1

        if tree[p]< tree[c]:
            tree[p], tree[c] = tree[c], tree[p]

        p = c
        c *= 2

    return tmp

tree = [0] * 101
last = 0
enq(3)
enq(2)
enq(4)
enq(7)
enq(5)
enq(1)

enq(9)
print(tree[:8])
print(tree[1])
while last > 0:
    print(deq(), tree[1])
