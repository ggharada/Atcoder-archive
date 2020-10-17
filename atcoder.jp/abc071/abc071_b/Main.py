s = input()
check = "abcdefghijklmnopqrstuvwxyz"

for i in range(len(s)):
    check = check.replace(s[i],"")

if len(check) == 0:
    print("None")
else:
    print(min(check))