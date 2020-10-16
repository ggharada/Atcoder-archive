c = [int(s) for s in input().split()]
c.sort(key=int)
if c[0] + c[3] == c[1] + c[2] or c[0] + c[1] + c[2] == c[3]:
    print("Yes")
else:
    print("No")