def solution(d, budget):
    answer = 0
    
    d.sort()
    
    for n in d:
        if n > budget:
            break
        
        answer += 1
        budget -= n
    
    return answer