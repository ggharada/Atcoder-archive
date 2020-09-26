a,b,c,d = map(int,input().split())

if a<= c <= b:
    print("Yes")
elif a<= d <= b:
    print("Yes")
elif c<= a <= d:
    print("Yes")
elif c<= b <= d:
    print("Yes")
else:
    print("No")