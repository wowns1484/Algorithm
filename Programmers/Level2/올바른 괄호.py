def solution(s):
    answer = True
    check = []
    
    s = list(s)
    if s.count('(') == s.count(')'):  
        for c in s:
            if c == "(":
                check.append(c)
            else:
                if len(check) == 0:
                    answer = False
                    break
                else:
                    check.pop()
    else:
        answer = False

    return answer