n,t = map(int,input().split())
count = t
a = []
for _ in range(n):a.append(int(input()))

for i in range(n-1):
    if a[i+1] - a[i] < t:
        count += a[i+1] - a[i]
    else:
        count += t
print(count)