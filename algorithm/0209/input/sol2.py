import sys
'''
    입력 값이 1이라면
    #1 True 출력
    #2 False
    
'''
sys.stdin = open('sol2.txt')

T = int(input()) #=> 10

#전체 테스트 케이스 수 만큼 반복

for tc in range(1, T+1):
    N = int(input())
    result = True if N%2 else False
    print(f'#{tc} {result}')