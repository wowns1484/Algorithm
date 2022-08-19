from itertools import permutations
import math

def solution(numbers):
    answer = 0
    nums = []
    
    for i in range(1, len(numbers) + 1):
        temp = set(permutations(list(numbers), i))

        for t in temp:
            t = ''.join(t)
            if t[0] != '0' and t != '1':
                nums.append(int(t))
            
    for n in nums:
        is_prime = True
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            answer += 1
    
    return answer