import sys

sys.stdin = open('input.txt', encoding='utf-8')

arr = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

def gns(array):
    return sorted(array, key=lambda x: arr.index(x))

T = int(input())
for tc in range(1, T+1):
    n, length = input().split()
    array = list(input().split())
    print(f'{n}')
    print(*gns(array))





