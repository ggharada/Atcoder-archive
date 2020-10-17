s = list(input())
check = []

for i in range(len(s)-2):
    check.append(abs(753 - int(s[i] + s[i+1] + s[i+2])))
print(min(check))