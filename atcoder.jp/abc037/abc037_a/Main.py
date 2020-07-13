a,b,c = map(int,input().split())
count = 0
while a <= c or b <= c:
    if a <= b:
        c -= a
        count += 1
    else:
        c -= b
        count += 1
print(count)