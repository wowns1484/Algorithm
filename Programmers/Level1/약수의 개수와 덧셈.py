def solution(left, right):
    answer = 0
    
    if left == 1:
        answer -= 1
        left += 1  
    
    for i in range(left, right+1):
        cnt = 2
        
        for j in range(2, i//2 + 1):
            if i % j == 0:
                cnt += 1
        
        if cnt % 2 == 1:
            answer -= i
        else:
            answer += i
            
    return answer