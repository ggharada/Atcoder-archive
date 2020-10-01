s = input()
for i in range(len(s)//2):
    if s[i] == s[-i-1]:
        pass
    elif s[i] == "*" or s[-i-1] == "*":
        pass
    else:
        print("NO")
        exit()
print("YES")