import sys
sys.stdin = open('input.txt')


E = int(input())
arr = list(map(int, input().split()))
V = E + 1

par = [0]*(V+1)
for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    par[c] = p

print(*par)

root = 0
for i in range(1, V+1):
    if par[i] == 0:
        root = i
        break
print(root)

# 조상 찾기
c = 5
anc = []
while par[c] != 0:
    anc.append(par[c])
    c = par[c]

# 정점 c의 조상 찾기
print(*anc)
print(anc[-1])