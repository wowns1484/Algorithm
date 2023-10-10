import sys

readline = sys.stdin.readline
write = sys.stdout.write

N = int(readline())

answers = [1, 3]

for i in range(2, N + 1):
    answers.append((answers[i - 1]*2 + answers[i - 2]) % 9901)

write(str(answers[-1]))