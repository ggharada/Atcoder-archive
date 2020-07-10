a,b = map(int,input().split())
check = []
check.append(a + b)
check.append(a - b)
check.append(a * b)
check.sort()
print(check[2])