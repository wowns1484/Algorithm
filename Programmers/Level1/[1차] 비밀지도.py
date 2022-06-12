def d_to_b(d, n):
    b = []

    idx = 0
    while(n > idx):
        b.append(d%2)
        d //= 2
        idx += 1
        
    b.reverse()
    
    return b

def solution(n, arr1, arr2):
    answer = []
    
    for n1, n2 in zip(arr1, arr2):
        cols = ""
        
        b1 = d_to_b(n1, n)
        b2 = d_to_b(n2, n)
        b = [a+b for a, b in zip(b1, b2)]
        
        for elem in b:
            if elem >= 1:
                cols += "#"
            else:
                cols += " "
        
        answer.append(cols)
    
    return answer