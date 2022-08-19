def solution(arr):
    arr.sort()
    cnt = 1
    
    while True:
        check = True
        num = arr[-1]*cnt
        
        for n in arr[:-1]:
            if num % n != 0:
                check = False
                break
               
        if check:
            return num
            
        cnt += 1