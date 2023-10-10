import sys

readline = sys.stdin.readline
write = sys.stdout.write

K, N = map(int, readline().split())
lines = []
max_line = 0

for _ in range(K):
    line = int(readline())
    lines.append(line)
    
    if max_line < line:
        max_line = line
        
l, r = 1, max_line

while l <= r:
    cnt = 0
    m = (l + r) // 2
    
    for line in lines:
        cnt += line // m
    
    if cnt < N:
        r = m - 1
    else:
        l = m + 1

write(str(r))