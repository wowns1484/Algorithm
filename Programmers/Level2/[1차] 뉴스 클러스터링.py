def solution(str1, str2):
    answer = 0
    
    s1, s2 = [], []

    for i in range(len(str1)-1):
        s = str1[i:i+2].upper()

        if 'Z' >= s[0] >= 'A' and 'Z' >= s[1] >= 'A':
            s1.append(s)

    for i in range(len(str2)-1):
        s = str2[i:i+2].upper()

        if 'Z' >= s[0] >= 'A' and 'Z' >= s[1] >= 'A' :
            s2.append(s)

    if not s1 and not s2:
        return 65536

    s11 = s1.copy()
    uni = s1.copy()
    for c in s2:
        if c not in s11:
            uni.append(c)
        else:
            s11.remove(c)

    inter = []
    for c in s2:
        if c in s1:
            s1.remove(c)
            inter.append(c)

    answer = int(len(inter)/len(uni)*65536)

    return answer