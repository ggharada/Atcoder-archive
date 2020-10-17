hp = int(input())
x = 1
n = 0
while(x <= hp):
    x *= 2
    n += 1
print(2**n - 1)