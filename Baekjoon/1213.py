import sys
from collections import Counter

readline = sys.stdin.readline
write = sys.stdout.write

counter = Counter(readline().rstrip())
counter = sorted(counter.items(), key=lambda x: x[0])

cnt = 0;
center = ""
s1, s2 = [], []
check = True

for key, value in counter:
    if value % 2 == 1:
        cnt += 1
        center = key

    n = value // 2
    s1.append(key*n)
    s2.append(key*n)
    
    if cnt == 2:
        check = False
        break

if check:
    write("".join(s1) + center + "".join(s2[::-1]))
else:
    write("I'm Sorry Hansoo")