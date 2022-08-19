from collections import defaultdict

def solution(clothes):
    answer = 1
    c = defaultdict(list)
    
    for cloth, key in clothes:
        c[key].append(cloth)
    
    for key in c.keys():
        answer *= len(c[key]) + 1
    
    return answer - 1