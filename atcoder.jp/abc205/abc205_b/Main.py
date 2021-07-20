n = int(input())
a = [int(s) for s in input().split()]
a.sort()
l = []
for i in range(n):
    l.append(i+1)

if a == l:
    print("Yes")
else:
    print("No")