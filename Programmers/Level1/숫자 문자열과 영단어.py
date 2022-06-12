def solution(s):
    answer = []
    
    num_check = ['0','1','2','3','4','5','6','7','8','9']
    alp_check = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    alphabet = ""
    for word in list(s):
        if word in num_check:
            answer.append(num_check[int(word)])
        else:
            alphabet += word
            
            if alphabet in alp_check:
                answer.append(num_check[alp_check.index(alphabet)])
                alphabet = ""
    
    return int(''.join(answer))