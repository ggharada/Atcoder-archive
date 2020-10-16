a,b = map(str,input().split())

for i in range(1,int(a+b)//2):
    if int(a+b) == i*i:
        print("Yes")
        exit()
print("No")