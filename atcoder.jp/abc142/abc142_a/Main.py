n = int(input())
array = 0
for i in range(1,n + 1):
    if i % 2 == 1:
        array += 1
print(array / n)