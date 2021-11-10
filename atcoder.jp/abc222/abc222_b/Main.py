n,p = map(int,input().split())
a = [int(s) for s in input().split()]
count = 0
for i in range(n):
    if a[i] < p:
        count += 1
print(count)