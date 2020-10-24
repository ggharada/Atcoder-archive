a,v = map(int,input().split())
b,w = map(int,input().split())
t = int(input())

diff = abs(a-b)
if (v - w) * t >= diff:
    print("YES")
else:
    print("NO")