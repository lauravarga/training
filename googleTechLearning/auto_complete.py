import sys

f = sys.stdin
n = int(f.readline())
words = [f.readline().strip() for _ in range(n)]
for _ in range(int(f.readline())):
    prefix = f.readline().strip()
    guess = []
    i = 0
    for w in words:
        if w.startswith(prefix):
            guess.append(w)
            i += 1
    print(' '.join(sorted(guess)))

