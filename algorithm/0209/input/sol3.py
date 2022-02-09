'''
입력받은 2차원 리스트의
(1,1) 을 불러 오시오
'''

import sys

sys.stdin = open('sol3.txt')

N = int(input())
array = []
for i in range(N):
    array.append(list(map(int,input().split())))

print(f'# { array[1][1]}')