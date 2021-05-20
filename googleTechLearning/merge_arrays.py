import sys

a, b = map(int, sys.stdin.readline().split())
ta = [int(sys.stdin.readline()) for _ in range(a)]
tb = [int(sys.stdin.readline()) for _ in range(b)]

# ... Replace this with actual merging.
result = []
i = 0
j = 0
for k in range(0, a + b):
    if i < len(ta):
        if j < len(tb):
            if ta[i] <= tb[j]:
                result.append(ta[i])
                i += 1
            else:
                result.append(tb[j])
                j += 1
        else:
            result.append(ta[i])
            i += 1
    else:
        result.append(tb[j])
        j += 1

for va in result:
    print(va)
