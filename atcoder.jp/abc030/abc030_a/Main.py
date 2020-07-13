a,b,c,d = map(int,input().split())
if a / b > c / d:
    print("AOKI")
elif a / b == c / d:
    print("DRAW")
else:
    print("TAKAHASHI")