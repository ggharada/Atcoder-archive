import math

k = int(input())

count = 0

for i in range(1,k+1):
    for j in range(1,k+1):
        for t in range(1,k+1):
            a = math.gcd(i, j)
            count += math.gcd(a,t)
print(count)