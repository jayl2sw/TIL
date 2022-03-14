import sys

sys.stdin = open('input.txt', encoding='utf-8')

arr = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

def gns3(array, length):
    result = []
    for n in range(10):
        for idx in range(int(length)):
            if array[idx] == arr[n]:
                result.append(arr[n])
    return result

T = int(input())
for tc in range(1, T+1):
    n, length = input().split()
    array = list(input().split())
    print(f'{n}')
    print(*gns3(array, length))





