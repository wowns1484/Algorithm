def solution(s, n):
    answer = ''
    
    up_cases = [chr(ord('A') + i) for i in range(26)]
    low_cases = [chr(ord('a') + i) for i in range(26)]

    for word in s:
        if word in up_cases:
            idx = (ord(word) - ord('A') + n) % 26
            word = up_cases[idx]
        elif word in low_cases:
            idx = (ord(word) - ord('a') + n) % 26
            word = low_cases[idx]
        
        answer += word
        
    return answer