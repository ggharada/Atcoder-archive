h,a = map(int,input().split())
counter = 0
while h > 0:
    h -= a
    counter += 1
print(counter)