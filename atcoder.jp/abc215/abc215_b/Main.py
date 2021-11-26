n = int(input())
ans = 0

for i in range(n):
    if 2**i <= n:
        ans = i
    else:
        break
print(ans)