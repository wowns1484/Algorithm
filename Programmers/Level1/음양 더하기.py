def solution(absolutes, signs):
    answer = 0
    
    for absolute, sign in zip(absolutes, signs):
        if sign == False:
            absolute = -absolute
        
        answer += absolute
    
    return answer