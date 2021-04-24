n = int(input())
a = [int(s) for s in input().split()]
b = [int(s) for s in input().split()]

count = []
flag = 0

for i in range(1001):
    for j in range(n):
        if a[j] <= i and i <= b[j]:
            flag = 0
        else:
            flag = 1
            break;
    if flag == 0:
        count.append(i)
    flag = 0

print(len(count))