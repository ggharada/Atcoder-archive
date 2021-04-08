s = input()
flag = 0

for i in range(len(s)):
    if i % 2 == 0:
        if s[i].isupper():
            flag = 1
    if i % 2 == 1:
        if s[i].islower():
            flag = 1
if flag == 1:
    print("No")
else:
    print("Yes")