N = int(input())
R = int(input())
input_list = [x for x in range(1, N+1)]
used = [0] * (N+1)


def permutation(arr, n):
    if n == len(input_list):
        print(arr)
        return
    for i in range(len(input_list)):
        if not used[i]:
            used[i] = 1
            arr.append(input_list[i])
            permutation(arr, n+1)
            arr.pop()
            used[i] = 0

permutation([], N-R)