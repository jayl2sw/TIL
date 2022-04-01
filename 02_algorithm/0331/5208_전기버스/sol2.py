T = int(input())
for tc in range(T+1):
    n, *arr = map(int, input().split())

    def recur(cur, c):
        ret = 0

        if cur >= n - 1:
            return ret

        if c == -1:
            return 100000000

        for i in range(c):
            ret = min(ret, recur(cur+i, c +arr[cur+i]))
        return ret

    print(recur(0, arr[0]))