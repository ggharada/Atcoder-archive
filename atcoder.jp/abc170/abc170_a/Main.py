line = list(input().split())
i = 0
while True:
    if line[i] == "0":
        print(i + 1)
        break
    else:
        i += 1