n = int(input())
cash = 0
for i in range(n):
    cash += (i + 1) * 10000 / n
print(round(cash))