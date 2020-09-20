x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())
count = 0
count += abs(x1 - x2)
count += abs(y1 - y2)
print(count + 1)