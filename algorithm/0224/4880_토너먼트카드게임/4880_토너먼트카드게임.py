import sys
sys.stdin = open('input.txt')

def card_game(a, b, refer):
    winner = (refer[a] - refer[b]) % 3
    if winner % 3 == 2:
        return b
    else:
        return a

def tournament(start, end, array):
    # array에 원소가 하나일 때,
    if start == end:
        return end

    # array에 원소가 2개 이상일 때,
    else:
        middle = (start + end) // 2
        return card_game(tournament(start, middle, array[:middle + 1]), tournament(middle + 1, end, array[middle+1:]), refer)

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    refer = list(map(int, input().split()))
    print(f'#{tc} {tournament(0, n-1, refer)+1}')


'''
        1
    2       3
  4   5   6    7
1 2  3 4  5 6  7 8

    1
  2     3
 4 5   6   7  
    
1 2 3 4 5 6
'''

