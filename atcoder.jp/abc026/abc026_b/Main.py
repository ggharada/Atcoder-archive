n = int(input())
tmp = [(int(input())) for _ in range(n)]
tmp.sort(key=int)
output = 0
for i in range(n):
    if i % 2 == 0:
        output += (tmp[i]) * (tmp[i]) * 3.14159
    else:
        output -= (tmp[i]) * (tmp[i]) * 3.14159
print(abs(output))