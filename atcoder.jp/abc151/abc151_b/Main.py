n,k,m = map(int,input().split())
a = [int(s) for s in input().split()]
tmp = 0
ans = 1000
for i in range(len(a)):
    tmp += a[i]
for i in range(k + 1):
    if (tmp + i) / n >= m:
        ans = i
        break
if ans == 1000:
    print(-1)
else:
    print(ans)