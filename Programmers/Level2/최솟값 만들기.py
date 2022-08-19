def solution(A,B):
    case_1, case_2 = 0, 0
    
    A.sort()
    B.sort(reverse=True)
    
    for a, b in zip(A, B):
        case_1 += a*b
        
    A.sort(reverse=True)
    B.sort()
    
    for a, b in zip(A, B):
        case_2 += a*b
    
    return min(case_1, case_2)