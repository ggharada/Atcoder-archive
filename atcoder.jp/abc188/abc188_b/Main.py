n = int(input())
a = [int(s) for s in input().split()]
b = [int(s) for s in input().split()]
s = 0
for i in range(n):
    s += a[i] * b[i]
if s == 0:
    print("Yes")
else:
    print("No")