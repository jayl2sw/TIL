import random


def binary_search(array, start, end, target):
    count = 0
    while True:
        middle = (start + end) // 2
        if middle == array.index(target):
            return middle + count
        elif middle < array.index(target):
            start = middle
            count += 1
        else:
            end = middle
            count += 1


def select_Presenter(problems):
    members = ['조원1', '조원2', '조원3', '조원4', '조원5']
    m = len(members)
    array = [0] * 40
    for problem in problems:
        array.insert(random.randint(0, len(array)), problem)

    for problem in problems:
        presenter = members[binary_search(array, 0, len(array), problem) % m]
        print(f'{presenter}이 {problem} 발표하시면 됩니다.')


select_Presenter(['회문1', '회문2'])