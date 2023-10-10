import sys

readline = sys.stdin.readline
write = sys.stdout.write

s = readline().rstrip()

answer = 'z'*len(s)
s1, s2, s3 = "", "", ""

for i in range(1, len(s) - 2):
    s1 = s[:i]
    for j in range(i + 1, len(s)):
        s2 = s[i:j]
        s3 = s[j:]

        temp = s1[::-1] + s2[::-1] + s3[::-1]

        if temp < answer:
            answer = temp
            
write(answer)