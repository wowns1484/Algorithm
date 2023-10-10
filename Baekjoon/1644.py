import sys

readline = sys.stdin.readline
write = sys.stdout.write

N = int(readline())

is_primes = [True]*(N + 1)
is_primes[0] = False
is_primes[1] = False

for i in range(2, int(N**0.5) + 1):
    j = i*i

    while j <= N:
        is_primes[j] = False
        j += i
        
primes = [i for i, prime in enumerate(is_primes) if prime]
answer = 0

for i in range(len(primes)):
    sum = 0
    for j in range(i, len(primes)):
        sum += primes[j]
        
        if sum == N:
            answer += 1
            break
        elif sum > N:
            break
    
write(str(answer))