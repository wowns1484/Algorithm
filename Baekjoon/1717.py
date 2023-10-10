import sys

sys.setrecursionlimit(100000)

readline = sys.stdin.readline
write = sys.stdout.write

n, m = map(int, readline().split())
parents = [i for i in range(n + 1)]

def find_parent(v):
    if parents[v] != v:
        parents[v] = find_parent(parents[v])
        
    return parents[v]

for _ in range(m):
    c, a, b = map(int, readline().split())
    a, b = find_parent(a), find_parent(b)
    
    if c:
        if a == b:
            write("YES\n")
        else:
            write("NO\n")
    else:
        if a > b:
            parents[a] = b
        else:
            parents[b] = a