import re

def solution(s):
    answer = []
    
    s = s.split("},{")
    s = sorted([re.sub(r"[{}]", "", c) for c in s], key=lambda x : len(x))

    for c in s:
        c = c.split(",")
        if len(answer) < len(s[-1].split(",")):
            for elem in c:
                elem = int(elem)
                if elem not in answer:
                    answer.append(elem)
        
    
    return answer