c = []
for _ in range(4):c.append(list(input().split()))
for i in reversed(range(0,4)):
    for j in reversed(range(0,4)):
        if j != 0:
            print(c[i][j] + " ",end="")
        else:
            print(c[i][j],end="")
    print()