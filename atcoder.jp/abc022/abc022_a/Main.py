n,s,t = map(int,input().split())
count = 0
tmp = 0
for i in range(n):
    tmp +=int(input())
    if tmp >= s and tmp <= t:
        count += 1
    else:
        pass
print(count)