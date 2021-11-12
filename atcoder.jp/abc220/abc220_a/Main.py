a,b,c = map(int,input().split())
x = c * (b//c)
if a <= x:
    print(x)
else:
    print(-1)