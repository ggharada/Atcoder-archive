a = int(input())
for i in range(101):
    if i*i*i == a:
        print("YES")
        exit(0)
else:
    print("NO")