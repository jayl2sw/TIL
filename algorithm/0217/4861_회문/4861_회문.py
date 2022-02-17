import sys
sys.stdin = open('input.txt')

def palindrome(string):
    l = len(string)
    for i in range(l//2):
        if string[i] != string[l-1-i]:
            return False
    return True

def find_palindrome_line(m, string):
    for i in range(len(string) - m + 1):
        check = string[i:i+m]
        if palindrome(check):
            return check

def reverse_array(n, array):
    for i in range(n):
        for j in range(n):
            if i<j:
                array[i][j],array[j][i] = array[j][i],array[i][j]

def find_palindrome(n, m, array):
    for i in range(n):
        result = find_palindrome_line(m, array[i])
        if result:
            return result

    reverse_array(n,array)

    for i in range(n):
        result = find_palindrome_line(m, array[i])
        if result:
            return result


T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(input()) for i in range(n)]
    print(f'#{tc} {"".join(find_palindrome(n, m, arr))}')
