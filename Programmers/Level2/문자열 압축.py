def solution(s):
    answer = 0
    result = []
    
    if len(s) == 1:
        answer = 1
    else:
        for i in range(1, len(s)):
            pre_s = s[:i]
            cnt = 1
            temp = ""
            
            for j in range(i, len(s), i):
                cur_s = s[j:j+i]

                if cur_s == pre_s:
                    cnt += 1
                    if j == len(s) - i:
                        temp += str(cnt) + pre_s
                else:
                    if cnt == 1:
                        temp += pre_s
                    else:
                        temp += str(cnt) + pre_s
                    cnt = 1
                
                pre_s = cur_s

            if len(cur_s) != i or temp[-i:] != cur_s:
                temp += cur_s

            result.append(len(temp))
            
        answer = min(result)

    return answer