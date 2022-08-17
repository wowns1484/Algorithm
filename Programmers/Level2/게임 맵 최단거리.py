from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])

    queue = deque([[0, 0]])
    visited = [[-1]*m for _ in range(n)]
    visited[0][0] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while(queue):
        y, x = queue.popleft()

        for d_x, d_y in zip(dx, dy):
            nx = x + d_x
            ny = y + d_y

            if 0 <= nx < m and 0 <= ny < n and maps[ny][nx] and visited[ny][nx] == -1:
                queue.append([ny, nx])
                visited[ny][nx] = visited[y][x] + 1
    
    return visited[n-1][m-1]