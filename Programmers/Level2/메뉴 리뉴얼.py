from itertools import combinations

def solution(orders, course):
    answer = []
    rec = {}
    
    for order in orders:
        order = list(order)
        
        for n in course:
            for menu in sorted(combinations(order, n)):
                menu = ''.join(sorted(menu))
            
                if menu not in rec:
                    rec[menu] = 1
                else:
                    rec[menu] += 1
    
    rec = sorted(rec.items(), key=lambda x:(len(x[0]), -x[1]))
    
    l, s = course[0], rec[0][1]
    for r in rec:
        if l < len(r[0]):
            l = len(r[0])
            s = r[1]
        
        if s == r[1] and s > 1:
            answer.append(r[0])
    
    answer.sort()

    return answer