n = int(input())

count = 100
for i in range(1,100+1):
    if i % n == 0:
        count -= 1
print(count)