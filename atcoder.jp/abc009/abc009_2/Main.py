n = int(input())
check = []
for _ in range(n):
    check.append(int(input()))
check = list(set(check))
check.sort(key=int)
print(check[-2])