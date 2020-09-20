n,k = map(int,input().split())
t = []
for i in range(n):
    t.append(int(input()))

for i in range(n - 2):
    if (t[i] + t[i+1] + t[i+2]) < k:
        print(i + 3)
        break
else:
    print(-1)