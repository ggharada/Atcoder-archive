d = [int(s) for s in input().split()]
j = [int(s) for s in input().split()]
count = 0
for i in range(7):
    if d[i] >= j[i]:
        count += d[i]
    else:
        count += j[i]
print(count)