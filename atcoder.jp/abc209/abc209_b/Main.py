n,x = map(int,input().split())
a = [int(s) for s in input().split()]

for i in range(n):
    if (i + 1) % 2 == 0:
        x -= (a[i] - 1)
    else:
        x -= a[i]
if x < 0:
    print("No")
else:
    print("Yes")