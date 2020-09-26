a = int(input())
b = int(input())
c = int(input())
s = int(input())

for i in range(a,a+2):
    for j in range(b,b+2):
        for t in range(c,c+2):
            if i + j + t == s:
                print("Yes")
                exit()
print("No")