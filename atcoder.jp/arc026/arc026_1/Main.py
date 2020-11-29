n,a,b = map(int,input().split())
maxcount = 5
timecount = 0

for i in range(n):
    if maxcount > 0:
        timecount += b
        maxcount -= 1
    else:
        timecount += a
print(timecount)