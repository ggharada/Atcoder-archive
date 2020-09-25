a,b,c,d = map(int,input().split())
check = []

check.append(a*c)
check.append(a*d)
check.append(b*c)
check.append(b*d)

print(max(check))