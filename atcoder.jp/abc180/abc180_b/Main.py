from decimal import Decimal

n = int(input())
x = [int(s) for s in input().split()]

m = []
for i in range(n):
    m.append(abs(x[i]))
print(sum(m))

u = 0
for i in range(n):
    u += pow(x[i],2)
print(Decimal(str(u))**Decimal("0.5"))

print(max(m))