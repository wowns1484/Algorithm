def solution(s):
    s = list(s)
    check = []
    check.append(s[0])
    
    for c in s[1:]:
        if len(check) > 0 and c == check[-1]:
            del check[-1]
        else:
            check.append(c)

    if len(check) == 0:
        answer = 1
    else:
        answer = 0

    return answer