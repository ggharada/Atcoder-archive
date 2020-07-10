a,b,c = map(int,input().split())
tmp = a - b
if c - tmp >= 0 :
    print(c - tmp)
else:
    print(0)