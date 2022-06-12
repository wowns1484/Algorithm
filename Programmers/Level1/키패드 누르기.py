def solution(numbers, hand):
    answer = ''
    
    left_num = [1,4,7]
    right_num = [3,6,9]
    
    now_L = 10
    now_R = 12
    
    matrix = []
    for i in range(4):
        for j in range(3):
            matrix.append((i,j))
    
    for number in numbers:
        if number in left_num:
            answer += 'L'
            now_L = number
        elif number in right_num:
            answer += 'R'
            now_R = number
        else:
            if number == 0:
                number = 11
                
            d_L = abs(matrix[now_L-1][0] - matrix[number-1][0]) + abs(matrix[now_L-1][1] - matrix[number-1][1])
            d_R = abs(matrix[now_R-1][0] - matrix[number-1][0]) + abs(matrix[now_R-1][1] - matrix[number-1][1])
            
            if d_L > d_R:
                answer += 'R'
                now_R = number
            elif d_L < d_R:
                answer += 'L'
                now_L = number
            else:
                if hand == 'right':
                    answer += 'R'
                    now_R = number
                else:
                    answer += 'L'
                    now_L = number
                
    return answer