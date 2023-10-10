import sys
from collections import defaultdict
import math
import heapq

readline = sys.stdin.readline
write = sys.stdout.write

N = int(readline())
M = int(readline())
edges = defaultdict(list)

for _ in range(M):
    a, b, c = map(int, readline().split())
    
    edges[a].append([b, c])
    
s, d = map(int, readline().split())
costs = [math.inf]*(N + 1)
costs[s] = 0

q = []
heapq.heappush(q, [0, s])

while q:
    c, n_s = heapq.heappop(q)
    
    if c > costs[n_s]:
        continue
    
    for n_d, n_c in edges[n_s]:
        if costs[n_d] > n_c + costs[n_s]:
            costs[n_d] = n_c + costs[n_s]
            heapq.heappush(q, [costs[n_d], n_d])
            
write(str(costs[d]))