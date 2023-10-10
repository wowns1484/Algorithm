import sys

readline = sys.stdin.readline
write = sys.stdout.write

M, N = map(int, readline().split())

primes = [True for _ in range(N + 1)]
primes[0] = False
primes[1] = False

for i in range(2, int(N**0.5) + 1):
    if primes[i]:
        idx = i*i
        
        while idx <= N:
            primes[idx] = False
            idx += i
            
primes = [idx for idx, prime in enumerate(primes) if prime and idx >= M]

for prime in primes:
    write(str(prime) + '\n')