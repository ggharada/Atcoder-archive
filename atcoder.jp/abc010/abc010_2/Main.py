n = int(input())
a = [int(s) for s in input().split()]

count = 0
toru = [0,0,1,0,1,2,3,0,1,0]
for i in range(n):
    count += toru[a[i]]
print(count)