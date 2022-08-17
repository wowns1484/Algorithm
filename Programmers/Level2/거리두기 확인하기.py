from collections import deque

def bfs(place):
    p = [[i, j] for j in range(5) for i in range(5) if place[i][j] == "P"]

    for s in p:
        queue = deque([[s[0], s[1], 0]])
        visited = [[0]*5 for _ in range(5)]
        visited[s[0]][s[1]] = 1

        while(queue):
            x, y, d = queue.popleft()

            dx = [0, 0, -1, 1]
            dy = [-1, 1, 0, 0]

            for d_x, d_y in zip(dx, dy):
                nx = x + d_x
                ny = y + d_y

                if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
                    if place[nx][ny] == "O":
                        queue.append([nx, ny, d + 1])
                        visited[nx][ny] = 1
                    
                    if place[nx][ny] == "P" and d < 2:
                        return 0

    return 1
    
def solution(places):
    answer = []
    
    for place in places:        
        answer.append(bfs(place))

    return answer
