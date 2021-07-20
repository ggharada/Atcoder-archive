x, y = map(int,input().split())
if x + y == 0:
    print(0)
elif x + y == 6:
    print(3)
elif x + y == 4:
    print(2)
elif x + y == 2:
    print(1)
else:
    print(3 - (x + y))