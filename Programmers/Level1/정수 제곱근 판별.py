import math

def solution(n):
    answer = -1

    check = math.sqrt(n)
    if check.is_integer():
        answer = int((check + 1)**2)

    return answer