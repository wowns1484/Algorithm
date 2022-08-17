def solution(rows, columns, queries):
    answer = []
    
    m = [[col + row*columns + 1 for col in range(columns)] for row in range(rows)]
    
    for idx, querie in enumerate(queries):
        x1, y1, x2, y2 = map(int, querie)
        n = m[x1-1][y1-1]
        ans = n

        for i in range(x1-1,x2-1):
            temp = m[i+1][y1-1]
            m[i][y1-1] = temp
            ans = min(ans, temp)

        for i in range(y1, y2):
            temp = m[x2-1][i]
            m[x2-1][i-1] = temp
            ans = min(ans, temp)

        for i in range(x2-1, x1-1, -1):
            temp = m[i-1][y2-1]
            m[i][y2-1] = temp
            ans = min(ans, temp)

        for i in range(y2-1, y1, -1):
            temp = m[x1-1][i-1]
            m[x1-1][i] = temp
            ans = min(ans, temp)

        m[x1-1][y1] = n

        answer.append(ans)

    return answer