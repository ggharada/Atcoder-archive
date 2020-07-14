import math
n = int(input())
a = list(map(int,input().split()))
output = 0
count = 0
for i in range(n):
    if a[i] > 0:
        output += a[i]
        count += 1
print(math.ceil(output / count))