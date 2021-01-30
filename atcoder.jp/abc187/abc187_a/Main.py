a,b = map(str,input().split())
sa,sb = 0,0
for i in range(len(a)):
    sa += int(a[i])
    sb += int(b[i])
print(max(sa,sb))