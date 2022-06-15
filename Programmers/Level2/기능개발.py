def solution(progresses, speeds):
    answer = []

    while(progresses):
        progresses = [x + y if x + y <= 100 else 100 for x, y in zip(progresses, speeds)]

        if 100 in progresses and progresses.index(100) == 0:
            cnt = 0
            for i in range(len(progresses)):
                if progresses[i] == 100:
                    cnt += 1
                else:
                    break

            del progresses[:cnt]
            del speeds[:cnt]
            
            answer.append(cnt)

    return answer