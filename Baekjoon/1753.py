import sys
from collections import defaultdict
import heapq
import math

readline = sys.stdin.readline
write = sys.stdout.write

V, E = map(int, readline().split())
K = int(readline())

edges = defaultdict(list)

for _ in range(E):
    u, v, w = map(int, readline().split())
    edges[u].append([v, w])

costs = [math.inf]*(V + 1)
costs[K] = 0
q = []
heapq.heappush(q, [0, K])

while q:
    c, n_k = heapq.heappop(q)

    if c > costs[n_k]:
        continue

    for n_v, n_w in edges[n_k]:
        if costs[n_v] > n_w + costs[n_k]:
            costs[n_v] = n_w + costs[n_k]
            heapq.heappush(q, [costs[n_v], n_v])
            
for cost in costs[1:]:
    if cost == math.inf:
        write("INF\n")
    else:
        write(str(cost) + '\n')