n = input()
sum0 = 0
for i in range(len(n)):
    sum0 += int(n[i])
if int(n) % sum0 == 0:
    print("Yes")
else:
    print("No")