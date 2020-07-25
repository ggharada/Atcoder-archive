n = int(input())
count = 0
for i in range(n):
    check = 0
    tmp = []
    tmp = list(input().split())
    for i in range(len(tmp)):
        check += int(tmp[i])
    if 0 <= check < 20:
        count += 1
print(count)