n = int(input())
ans = 1
anscount = 0
count = 0

for i in range(1,n+1):
    count = 0
    j = i
    while i % 2 == 0:
        count += 1
        if anscount < count:
            anscount = count
            ans = j
        i /= 2
print(ans)