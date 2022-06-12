from itertools import combinations

def isPrime(n):
    if n == 0 or n == 1:
        return False
    else:
        for i in range(2, (n//2) + 1):
            if n % i == 0:
                return False

        return True

def solution(nums):
    answer = 0
    
    nums = list(combinations(nums, 3))
    
    for num in nums:
        if isPrime(sum(num)):
            answer += 1 

    return answer