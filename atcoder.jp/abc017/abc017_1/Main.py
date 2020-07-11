a1,a2 = map(int,input().split())
b1,b2 = map(int,input().split())
c1,c2 = map(int,input().split())
tmp = 0
tmp += a1 * a2 / 10
tmp += b1 * b2 / 10
tmp += c1 * c2 / 10
print(round(tmp))