import sys
from collections import deque

readline = sys.stdin.readline
write = sys.stdout.write

T = int(readline())

def bfs(baechu, x, y):
    q = deque([(x, y)])
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while q:        
        cx, cy = q.popleft()
                
        for nx, ny in zip(dx, dy):
            x, y = cx + nx, cy + ny
            
            if 0 <= x < M and 0 <= y < N and baechu[y][x] == 1:
                q.append([x, y])
                baechu[y][x] = 0

for _ in range(T):
    M, N, K = map(int, readline().split())
    
    baechu = [[0 for _ in range(M)] for _ in range(N)]
    candidates = []
    
    for _ in range(K):
        x, y = map(int, readline().split())
        
        baechu[y][x] = 1
        candidates.append([x, y])
    
    answer = 0
    
    for x, y in candidates:
        if baechu[y][x] == 1:
            bfs(baechu, x, y)
            answer += 1
            
    write(str(answer) + "\n")