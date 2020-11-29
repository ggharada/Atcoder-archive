y = int(input())

flag = 4

if y % 4 == 0:
    flag = 1
if y % 100 == 0:
    flag = 2
if y % 400 == 0:
    flag = 3

if flag % 2 == 0:
    print("NO")
else:
    print("YES")