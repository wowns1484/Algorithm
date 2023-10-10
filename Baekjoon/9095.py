import sys

readline = sys.stdin.readline
write = sys.stdout.write

T = int(readline())

for _ in range(T):
    N = int(readline())
    answer = [1, 1, 2] + [0]*(N - 2)
    
    for i in range(3, N + 1):
        answer[i] = answer[i - 1] + answer[i - 2] + answer[i - 3]
            
    write(str(answer[N]) + '\n')