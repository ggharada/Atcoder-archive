n,k = map(int,input().split())
h = [int(s) for s in input().split()]
count = 0
for i in range(n):
    if h[i] >= k:
        count += 1
print(count)