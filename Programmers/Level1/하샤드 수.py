def solution(x):
    answer = True

    check = 0
    n = x
    while n:
        check += n % 10
        n //= 10

    if x % check != 0:
        answer = False

    return answer