import sys

readline = sys.stdin.readline
write = sys.stdout.write

N = int(readline())
arr = set(map(int, readline().split()))

M = int(readline())
checks = list(map(int, readline().split()))


for check in checks:
    if check in arr:
        write('1\n')
    else:
        write('0\n')