import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    
    while(len(scoville) >= 2):   
        ori1 = heapq.heappop(scoville)
        
        if ori1 >= K:
            break
        
        ori2 = heapq.heappop(scoville)
        new = ori1 + ori2*2
        heapq.heappush(scoville, new)
        
        answer += 1
        
    if scoville[0] < K:
        answer = -1
    
    return answer