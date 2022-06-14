def solution(s):
    answer = ''

    idx = 0
    for word in s:
        if word == " ":
            answer += word
            idx = 0
        elif idx % 2 == 0:
            answer += word.upper()
            idx += 1
        else:
            answer += word.lower()
            idx += 1

    return answer