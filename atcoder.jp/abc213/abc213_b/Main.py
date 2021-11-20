n = int(input())
a = [int(s) for s in input().split()]

tmp = (max(a))
a[a.index(tmp)] = 0
tmp = (max(a))
print(a.index(tmp) + 1)