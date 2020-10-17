n = int(input())
w = [int(s) for s in input().split()]
check = []
for t in range(n):
    s1 = sum(w[:t])
    s2 = sum(w[t:])
    check.append(abs(s1-s2))
print(min(check))