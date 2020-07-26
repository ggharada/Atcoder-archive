x,y = map(int,input().split())
k = int(input())
if y - k >= 0:
    print(x + k)
else:
    print(x + y * 2 - k)