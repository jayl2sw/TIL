import sys
sys.stdin = open('input.txt')

def card_game(a, b, refer):
    if refer[a] == 3:
        if refer[b] == 1:
            return b
        else:
            return a
    elif refer[b] == 3:
        if refer[a] == 1:
            return a
        elif refer[a] == 2:
            return b
    else:
        if refer[a] >= refer[b]:
            return a
        else:
            return b

def tournament(start, end, array):
    if start == end:
        return end
    if len(array) == 2:
        return card_game(start, end, refer)
    else:
        middle = (start + end) // 2
        return card_game(tournament(start, middle, array[:middle + 1]), tournament(middle + 1, end, array[middle+1:]), refer)

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    refer = list(map(int, input().split()))
    print(f'#{tc} {tournament(0, n-1, refer)+1}')




