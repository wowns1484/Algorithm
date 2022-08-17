from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque([(numbers[0], 0), (-1*numbers[0],  0)])
    
    while queue:
        temp, idx = queue.popleft()
        
        if idx < len(numbers) - 1:
            queue.append([temp + numbers[idx + 1], idx + 1])
            queue.append([temp - numbers[idx + 1], idx + 1])
        else:
            if temp == target:
                answer += 1

    return answer