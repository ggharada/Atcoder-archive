n,a,b = map(int,input().split())

place = 0
for i in range(n):
    s,d = map(str,input().split())
    d = int(d)
    if s == "East":
        if d < a:
            place += a
        elif a <= d <= b:
            place += d
        else:
            place += b
    else:
        if d < a:
            place -= a
        elif a <= d <= b:
            place -= d
        else:
            place -= b

if place == 0:
    print(0)
elif place > 0:
    print("East " + str(place))
else:
    print("West " + str(abs(place)))