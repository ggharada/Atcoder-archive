n = int(input())
check = 2025 - n
for i in range(10):
    for j in range(10):
        if i * j == check:
            print(str(i) + " x " + str(j))