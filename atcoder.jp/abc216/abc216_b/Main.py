n = int(input())
ans = "No"
s = [0] * n
t = [0] * n

for i in range(n):
    s[i], t[i] = map(str, input().split())

for i in range(n):
    for j in range(i + 1, n):
        if s[i] == s[j] and t[i] == t[j]:
            ans = "Yes"
print(ans)