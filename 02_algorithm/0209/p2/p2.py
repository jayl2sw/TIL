import sys

sys.stdin = open('input.txt')

T = int(input())


def check_babygin(numbers):
    is_babygin = 0
    counter = [0 for _ in range(10)]

    for number in numbers:
        counter[number] += 1

    idx = 0
    while idx < len(counter):
        if counter[idx] >= 3:
            counter[idx] -= 3
            is_babygin += 1
            continue

        if idx < len(counter)-2:
            if counter[idx] and counter[idx+1] and counter[idx+2]:
                counter[idx] -= 1
                counter[idx+1] -= 1
                counter[idx+2] -= 1
                is_babygin += 1
                continue

        idx += 1

        if is_babygin == 2:
            return 1

    return 0


for tc in range(1, T+1):
    numbers = list(map(int, input()))
    result = "Baby Gin" if check_babygin(numbers) else "Lose"
    print(f'#{tc} {result}')