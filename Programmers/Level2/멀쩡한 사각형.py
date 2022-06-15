import math

def solution(w,h):
    g = math.gcd(w, h)
    answer = w*h - (w + h - g)

    return answer