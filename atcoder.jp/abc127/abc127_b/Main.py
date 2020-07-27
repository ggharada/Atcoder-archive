r,d,x = map(int,input().split())
for i in range(1,11):
    x = x * r - d
    print(x)