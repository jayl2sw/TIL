def check_bracket(string):
    array = []
    for char in string:
        if char == '(':
            array.append('(')
        elif char == ')':
            if array:
                array.pop()
            else:
                return False

    if not array:
        return True
    else:
        return False


