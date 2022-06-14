def solution(n):
    answer = []

    while(n > 0):
        answer.append(str(n % 10))
        n //= 10

    answer = sorted(answer, reverse=True)

    return int(''.join(answer))