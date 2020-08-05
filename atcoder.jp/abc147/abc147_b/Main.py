s = input()
diffcount = 0
for i in range(len(s)//2):
    if s[i] != s[-(i + 1)]:
        diffcount += 1
print(diffcount)