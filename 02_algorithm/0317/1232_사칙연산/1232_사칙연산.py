import sys
sys.stdin = open('input.txt')
# def calculate(oper, num1, num2):
#     if oper == "+":
#         return int(num1) + int(num2)
#     elif oper == "-":
#         return int(num1) - int(num2)
#     elif oper == "*":
#         return int(num1) * int(num2)
#     else:
#         return int(num1) / int(num2)
#
# def solution(N):
#     N = int(N)
#     if type(tree[N]) == tuple:
#         tmp = calculate(tree[N][0], solution(tree[N][1][0]), solution(tree[N][1][1]))
#         return int(tmp)
#     else:
#         return int(tree[N])

def solution(N):
    N = int(N)
    if type(tree[N]) == tuple:
        tmp = eval(f'{solution(tree[N][1][0])}{tree[N][0]}{solution(tree[N][1][1])}')
        return int(tmp)
    else:
        return int(tree[N])



for tc in range(1, 11):
    N = int(input())
    tree = [-1] * (N+1)
    operator = ['+', '-', '*', '/']
    for i in range(N):
        n, x, *args = input().split()
        if args:
            tree[int(n)] = x, args
        else:
            tree[int(n)] = x

    print(f'#{tc} {solution(1)}')
