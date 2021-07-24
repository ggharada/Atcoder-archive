a,b,c,d = map(int,input().split())

if b >= c * d:
    print(-1)
else:
    print(-(-a//(c * d - b)))