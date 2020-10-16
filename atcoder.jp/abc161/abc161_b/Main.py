n,m = map(int,input().split())
a = [int(s) for s in input().split()]
total = sum(a)
check = total/(4*m)
point = 0

for i in range(len(a)):
    if a[i] >= check:
        point += 1
print("Yes") if m <= point else print("No")