import sys

readline = sys.stdin.readline
write = sys.stdout.write

N = int(readline())
lines = []

for _ in range(N):
    A, B = map(int, readline().split())
    lines.append([A, B])
    
lines = sorted(lines, key=lambda x: x[0])
answer = [1]*N

for i in range(N):
    for j in range(i):
        if lines[i][1] > lines[j][1]:
            answer[i] = max(answer[i], answer[j] + 1)
            
write(str(N - max(answer)))