s = input()
for i in range(len(s)):
    if s[i] == "O" or s[i] == "D":
        print(0,end="")
    elif s[i] == "I":
        print(1,end="")
    elif s[i] == "Z":
        print(2,end="")
    elif s[i] == "S":
        print(5,end="")
    elif s[i] == "B":
        print(8,end="")
    else:
        print(s[i],end="")
print("")