from collections import deque

def solution(priorities, location):
    answer = 1
    priorities = deque([(prioritie, idx) for idx, prioritie in enumerate(priorities)])
    
    while priorities:
        elem = priorities.popleft()

        if priorities and elem[0] < max(priorities)[0]:
            priorities.append(elem)
        elif elem[1] == location:
            break
        else:
            answer += 1
            
    return answer