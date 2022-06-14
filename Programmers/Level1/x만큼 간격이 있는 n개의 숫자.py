def solution(x, n):
    answer = []

    if x == 0:
        answer = [0] * n
    else:
        ab_x = abs(x)
        for i in range(ab_x, ab_x*n +1, ab_x):
            if x < 0 :
                i *= -1
            answer.append(i)

    return answer