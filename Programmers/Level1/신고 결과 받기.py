def solution(id_list, report, k):
    answer = []
    result = {}
    report = set(report)
    acc_report = {}
    
    for id in id_list:
        result[id] = []
    
    for elem in report:
        split_elem = elem.split(" ")
        user = split_elem[0]
        reported = split_elem[1]
        
        result[user].append(reported)
        
        if reported in acc_report:
            acc_report[reported] += 1
        else:
            acc_report[reported] = 1
            
    for id in id_list:
        cnt = 0
        
        for elem in result[id]:
            if acc_report[elem] >= k:
                cnt += 1
        
        answer.append(cnt)
    
    return answer