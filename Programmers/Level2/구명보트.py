from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    people = deque(people)

    while people:        
        if len(people) == 1:
            answer += 1
            break
        
        if people[0] + people[-1] > limit:
            people.pop()
        else:
            people.pop()
            people.popleft()
       
        answer += 1
            
    return answer