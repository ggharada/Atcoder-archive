x,y = map(int, input().split())
if y % 2 == 1:
    print("No")
elif 2 * x <= y <= 4 * x:
    print("Yes")
else:
    print("No")