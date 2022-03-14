import sys
sys.stdin = open('extra_input.txt')

def rate(char):
    if char == '*' or char == '/':
        return 2
    elif char == '+' or char == '-':
        return 1
    elif char == '(':
        return 0

def manage_stack_char(stack, char):
    global result
    if not stack:
        stack.append(char)
    else:
        if rate(char) > rate(stack[-1]):
            stack.append(char)
        else:
            while rate(stack[-1]) >= rate(char):
                result += stack.pop()
                if not stack:
                    break
            if not stack:
                pass
            elif stack[-1] == '(':
                stack.pop()
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


    for i in range(len(stack)):
        result += stack.pop()

    return result


T = int(input())
for tc in range(1, T+1):
    string = input()
    result = ''
    print(f'#{tc} {change_to_postfix(string)}')