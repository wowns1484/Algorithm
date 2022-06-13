import math
import re

def solution(dartResult):
    answer = []

    bonus = {}
    bonus['S'] = 1
    bonus['D'] = 2
    bonus['T'] = 3
    
    scores = re.findall('\d+', dartResult)
    obs = re.sub('[^a-zA-Z|*#]', ' ', dartResult).split(' ')
    obs = [ob for ob in obs if ob != '']

    for idx, (score, ob) in enumerate(zip(scores, obs)):
        answer.append(int(math.pow(int(score), bonus[ob[0]])))
        
        if len(ob) == 2:
            if ob[1] == '*':
                answer[idx] *= 2

                if idx != 0:
                    answer[idx-1] *= 2
            else:
                answer[idx] *= -1

    return sum(answer)