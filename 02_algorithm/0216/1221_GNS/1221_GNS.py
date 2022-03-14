import sys

sys.stdin = open('input.txt', encoding='utf-8')

arr = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

def counting_sort(array):
    temp = [0]*10
    for num in array:
        temp[arr.index(num)] += 1

    for nnum in range(len(arr)):
        for _ in range(temp[nnum]):
            print(arr[nnum], end=' ')

T = int(input())
for tc in range(1, T+1):
    n, length = input().split()
    array = list(input().split())
    print(f'{n}')
    counting_sort(array)
    print()





