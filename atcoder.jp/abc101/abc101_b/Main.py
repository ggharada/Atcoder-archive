n = input()
check = 0
for i in range(len(n)):
    check += int(n[i])
if int(n) % check == 0:
    print("Yes")
else:
    print("No")