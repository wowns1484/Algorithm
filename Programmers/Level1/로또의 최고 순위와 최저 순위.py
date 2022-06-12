def solution(lottos, win_nums):
    answer = []
    
    result = [6,6,5,4,3,2,1]
    
    cnt = 0
    x_cnt = 0
    for lotto in lottos:
        if lotto in win_nums:
            cnt += 1
        elif lotto == 0:
            x_cnt += 1
        
    answer.append(result[cnt + x_cnt])
    answer.append(result[cnt])
    
    return answer