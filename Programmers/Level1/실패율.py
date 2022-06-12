def solution(N, stages):
    progress = {}
    
    total_p = len(stages)
    
    for n in range(N):
        cur_p = stages.count(n+1)
        
        if cur_p == 0:
            progress[n+1] = 0
        else:
            progress[n+1] = cur_p / total_p

            total_p -= cur_p
    
    progress = sorted(progress.items(), key=lambda item: item[1], reverse=True)
    answer = list(elem[0] for elem in progress)
    
    return answer