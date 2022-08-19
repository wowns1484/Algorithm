def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    
    for idx, citation in enumerate(citations):
        if idx + 1 > citation:
            break
            
        answer = idx + 1
        
    return answer