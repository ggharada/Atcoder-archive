count = 0
for _ in range(12):
    inline = list(input())
    for j in range(len(inline)):
        if inline[j] == "r":
            count += 1
            break
print(count)