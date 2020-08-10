x,y = map(int,input().split())
if x > 0 and y > 0:
    print(y - x)
elif x < 0 and y > 0:
    print(abs(y - x - 1))
else:
    print(abs(y - x))