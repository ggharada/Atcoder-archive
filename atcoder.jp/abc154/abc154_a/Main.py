s,t = input().split()
a,b = map(int,input().split())
u = input()
if u == s:
    print(str(a - 1) + " " + str(b))
else:
    print(str(a) + " " + str(b - 1))