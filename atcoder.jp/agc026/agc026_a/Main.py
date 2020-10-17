n = int(input())
a = [int(s) for s in input().split()]

count = 0
for i in range(n-1):
    if a[i] == a[i+1]:
        count += 1
        a[i+1] += 100
print(count)