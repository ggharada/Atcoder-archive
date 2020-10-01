n = int(input())
a,b,c = input(),input(),input()

ans = 0
for i in range(n):
    diff = len(set((a[i], b[i], c[i])))
    ans += diff - 1
print(ans)