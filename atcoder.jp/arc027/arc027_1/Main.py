h,m = map(str,input().split())
h = (17 - int(h)) * 60
m = 60 -  int(m)
print(int(h + m))