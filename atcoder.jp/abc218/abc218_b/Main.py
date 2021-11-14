p = [int(s) for s in input().split()]
abc = "abcdefghijklmnopqrstuvwxyz"
for i in range(len(p)):
    print(abc[p[i] - 1], end="")
print()