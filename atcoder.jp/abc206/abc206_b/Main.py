n = int(input())
coin = 0
i = 0
while True:
    i += 1
    coin += i
    if coin >= n:
        break
print(i)