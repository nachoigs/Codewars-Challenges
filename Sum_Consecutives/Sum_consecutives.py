def sum_consecutives(s):
    prev_num = None
    result = []
    for num in s:
        if num == prev_num:
            result[-1] += num
        else:
            result.append(num)
        prev_num = num

    return result
