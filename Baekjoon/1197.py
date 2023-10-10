import sys

readline = sys.stdin.readline
write = sys.stdout.write

V, E = map(int, readline().split())

edges = []

for _ in range(E):
    A, B, C = map(int, readline().split())
    edges.append([A, B, C])

edges = sorted(edges, key=lambda x : x[2])
parents = [i for i in range(V + 1)]

def find_parent(V):
    if V != parents[V]:
        parents[V] = find_parent(parents[V])

    return parents[V]

answer, cnt = 0, 1

for edge in edges:
    parent_a, parent_b = find_parent(edge[0]), find_parent(edge[1])

    if parent_a != parent_b:
        if parent_a < parent_b:
            parents[parent_b] = parent_a
        elif parent_a > parent_b:
            parents[parent_a] = parent_b

        answer += edge[2]
        cnt += 1

    if cnt == V:
        break

write(str(answer))