line = list(input())
if len(line) == 1:
    if line[0] == "a":
        print(-1)
    else:
        print("a")
else:
    print("".join(line[0:-1]))