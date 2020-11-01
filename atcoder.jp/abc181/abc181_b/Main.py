count = 0
for i in range(int(input())):
    a,b = map(int,input().split()) 
    count += int(b * (b + 1) / 2) - int(a * (a + 1) / 2) + a
print(count)