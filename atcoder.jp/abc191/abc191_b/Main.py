n, x = map(int,input().split())
a = [int(s) for s in input().split()]

for i in range(n):
    if a[i] != x:
        print(a[i],end=" ")
print("")