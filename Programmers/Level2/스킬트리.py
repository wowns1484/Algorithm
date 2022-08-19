def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        temp = list(skill).copy()
        
        check = True
        for s in skill_tree:
            if s in temp and s == temp[0]:
                temp.pop(0)
            elif s in temp and s != temp[0]:
                check = False
                break
    
        if check:
            answer += 1
    
    return answer