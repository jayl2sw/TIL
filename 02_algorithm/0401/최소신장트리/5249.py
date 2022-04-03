import sys
sys.stdin = open('input.txt')


def findset(x):
    if x == p[x]:
        return x
    else:
        return findset(p[x])


def mst():
    c = 0 # 간선의 개수
    cost = 0 #가중치의 합
    i = 0

    #MST를 구성하는 V 개의 간선
    while c < V:
        p1 = findset(arr[i][0])
        p2 = findset(arr[i][1])

        if p1 != p2:
            cost += arr[i][2]
            c += 1
            p[p2] = p1
        i += 1
        print(p)
    return cost

T = int(input())
for tc in range(1, T+1):
    V, E = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(E)]

    print(arr)
    arr.sort(key=lambda x: x[2])
    print(arr)
    p = list(range(V+1))
    print(p)

    print(mst())
