import sys
from collections import Counter

readline = sys.stdin.readline
write = sys.stdout.write

N, M = map(int, readline().split())
trees = Counter(list(map(int, readline().split())))
l, r = 0, 1e9

while l <= r:
    sum = 0
    m = (l + r) // 2
    
    for tree in trees:
        sub = tree - m
        
        if sub > 0:
            sum += sub*trees[tree]
    
    if sum < M:
        r = m - 1
    else:
        l = m + 1
    
    
write(str(int(r)))