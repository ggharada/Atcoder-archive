import math

n = int(input())
a = [int(s) for s in input().split()]
result = [0]*1010

for k in range(2,1001):
    gcd = 0
    for i in range(len(a)):
        if a[i] % k == 0:
            gcd += 1
    result[k] = gcd
print(result.index(max(result)))