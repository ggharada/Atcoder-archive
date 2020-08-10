s = input().split()
for i in range(len(s)):
    if s[i] == "Left":
        print("<",end="")
    elif s[i] == "Right":
        print(">",end="")
    else:
        print("A",end="")
    if i + 1 != len(s):
        print(" ",end="")
    else:
        print()