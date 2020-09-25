n = int(input())
m = [int(s) for s in input().split()]

need = 0
for i in range(n):
    if m[i] < 80:
        need += 80 - m[i]
print(need)