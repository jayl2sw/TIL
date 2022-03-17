import sys
sys.stdin = open('input.txt')

# heap 에 넣는 함수
def in_heap(N):
    c = len(heap)
    heap.append(N)
    p = c//2

    while p >= 1:
        if heap[p] > heap[c]:
            heap[p], heap[c] = heap[c], heap[p]
        else:
            break
        c = p
        p = c // 2

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    heap = [-1]

    for number in arr:
        in_heap(number)

    result = 0
    k = len(heap) - 1
    while k > 1:
        k = k // 2
        print(heap[k])
        result += heap[k]

    print(f'#{tc} {result}')