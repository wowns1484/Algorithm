import sys
from collections import defaultdict, deque

readline = sys.stdin.readline
write = sys.stdout.write

N, M = map(int, readline().split())

computers = defaultdict(list)

for _ in range(M):
    A, B = map(int, readline().split())
    
    computers[B].append(A)

max_cnt = 0
cnts = []

for i in range(1, N + 1):
    q = deque([i])
    visited = [False]*(N + 1)
    visited[i] = True
    cnt = 0;
    
    while q:
        v = q.popleft()
        
        for computer in computers[v]:
            if visited[computer] == False:
                visited[computer] = True
                cnt += 1
                q.append(computer)

    if max_cnt < cnt:
        max_cnt = cnt
        
    cnts.append([i, cnt])

for v, cnt in cnts:
    if cnt == max_cnt:
        write(str(v) + " ")