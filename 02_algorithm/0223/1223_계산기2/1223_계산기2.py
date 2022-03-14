import sys
sys.stdin = open('input.txt')


def manage_stack_char(stack, char):
    rate = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}
    global result
    if not stack:
        stack.append(char)
    else:
        if rate[char] > rate[stack[-1]]:
            stack.append(char)
        else:
            while rate[stack[-1]] >= rate[char]:
                result += stack.pop()
                if not stack:
                    break
            if not stack:
                pass
            stack.append(char)


def change_to_postfix(string):
    global result
    non_number = ['+', '-', '*', '/', '(', ')']
    stack = []

    for char in string:
        if char == '(':
            stack.append(char)

        elif char == ')':
            if not stack:
                raise 'Wrong String'
            while stack[-1] != '(':
                result += stack.pop()
                if not stack:
                    break
            stack.pop()

        elif char not in non_number:
            result += char

        elif char == '*' or char == '/':
            manage_stack_char(stack, char)

        elif char == '+' or char == '-':
            manage_stack_char(stack, char)


    while len(stack)>1:
        result += stack.pop()

    return result


def operate(a, b, operator):
    if operator == '+':
        return a+b
    elif operator == '-':
        return a-b
    elif operator == '*':
        return a*b
    elif operator == '/':
        return a/b


def calculate(string):
    operator = ['+', '-', '*', '/']
    preprocess = list(change_to_postfix(string))
    stack = []
    for char in preprocess:
        if char not in operator:
            stack.append(char)
        else:
            a = int(stack.pop())
            b = int(stack.pop())
            stack.append(operate(a, b, char))

    return stack[0]



for tc in range(1, 11):
    n = int(input())
    string = input()
    result = ''
    print(f'#{tc} {calculate(string)}')
