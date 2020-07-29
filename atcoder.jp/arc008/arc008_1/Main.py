import math

n = int(input())
if n % 10 < 7:
    money = math.ceil(n // 10) * 100
    money += n % 10 * 15
else:
    money = math.floor(n // 10) * 100 + 100
print(money)