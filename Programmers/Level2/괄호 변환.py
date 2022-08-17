def split(p):
    o_cnt, c_cnt = 0, 0

    for i in range(len(p)):
        if p[i] == '(':
            o_cnt += 1
        else:
            c_cnt += 1

        if o_cnt == c_cnt:
            return p[:i+1], p[i+1:]

def correct(u):
    s = []

    for c in u:
        if c == '(':
            s.append(c)
        else:
            if not s:
                return False
            s.pop()
        
    return True

def solution(p):
    if not p:
        return ''

    u, v = split(p)

    if correct(u):
        return u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = u[1:-1]
        
        for c in u:
            if c == '(':
                answer += ')'
            else:
                answer += '('
        
        return answer