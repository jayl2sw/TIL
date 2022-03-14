result = []
def powerset(arr, idx, temp, cnt):
    if len(temp) == cnt:
        result.append(temp)
        return
    elif len(temp) > cnt:
        return

    else:
        powerset()
