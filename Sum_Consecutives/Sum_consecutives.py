def sum_consecutives(s):
    sum = s[0]
    result = s[0] if (not range(len(s)-1)) else []
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            sum += s[i+1]
            if (i == len(s)-2):
                result.append(sum)
        else:
            result.append(sum)
            sum = s[i+1]
            if (i == len(s)-2):
                result.append(sum)
    return result
