n = int(input())
if (n - 1) // 20 % 2 == 0:
    print((n - 1) % 20 + 1)
else:
    print(20 - (n - 1) % 20)