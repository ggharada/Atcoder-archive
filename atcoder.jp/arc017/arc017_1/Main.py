n = int(input())
flag = 0
for i in range(2,n):
    if n % i == 0 != n:
        print("NO")
        break
else:
    print("YES")