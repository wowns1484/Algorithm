def solution(n, m):
    answer = []

    x, y = n, m
    while y:
        x, y = y, x % y 
    
    answer.append(x)

    a, b = n, m
    while(a != b):
        if a < b:
            a += n
        else:
            b += m
    
    answer.append(a)

    return answer