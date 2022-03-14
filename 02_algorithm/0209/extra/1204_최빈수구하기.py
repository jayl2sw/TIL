import sys

sys.stdin = open('input.txt')

def most(arr):
    scores = [0]* 101
    for i in range(len(arr)):
        scores[arr[i]] += 1

    max_score = max(scores)
    return len(scores) - scores[::-1].index(max_score) -1




N = int(input())
for tc in range(1, N+1):
    no = int(input())
    array = list(map(int, input().split()))
    result = most(array)
    print(f'#{tc} {result}')

