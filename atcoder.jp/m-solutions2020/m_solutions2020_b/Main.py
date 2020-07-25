a,b,c = map(int,input().split())
k = int(input())
count = 0
for i in range(k):
    if b <= a:
        b = b * 2
        count += 1
    elif a < b and c <= b:
        c = c * 2
        count += 1
    if count == k:
        break

if a < b and b < c:
    print("Yes")
else:
    print("No")