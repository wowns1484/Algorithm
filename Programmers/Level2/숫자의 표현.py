def solution(n):
    answer = 0
    
    for i in range(n):
        s = 0
        for j in range(i+1, n+1):
            s += j
            
            if s > n:
                break
            if s == n:
                answer += 1 
                break
            
    return answer