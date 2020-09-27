s = input()
a,b,c,d = map(int,input().split())
for i in range(len(s)):
    if a == i or b == i or c == i or d == i:
        print('"',end="")
    print(s[i],end="")
if len(s) == d:
    print('"')
else:
    print()