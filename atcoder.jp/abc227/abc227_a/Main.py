n,k,a = map(int,input().split())
ans = a - 1
for _ in range(k):
    ans += 1
    if ans > n:
        ans = 1
print(ans)