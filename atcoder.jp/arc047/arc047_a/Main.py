n,l = map(int,input().split())
s = input()
tabcount = 1
clashcount = 0
for i in range(n):
    if s[i] == "+":
        tabcount += 1
    else:
        tabcount -= 1
    if tabcount > l:
        tabcount = 1
        clashcount += 1
print(clashcount)