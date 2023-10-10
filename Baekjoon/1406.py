import sys

readline = sys.stdin.readline
write = sys.stdout.write

s1, s2 = list(readline().rstrip()), []
M = int(readline())

for _ in range(M):
    command = readline().rstrip()
    
    if command == "L" and s1:
        s2.append(s1.pop())
    elif command == "D" and s2:
        s1.append(s2.pop())
    elif command == "B" and s1:
        s1.pop()
    elif command[0] == "P":
        s1.append(command[2])
    
write(''.join(s1 + s2[::-1]))