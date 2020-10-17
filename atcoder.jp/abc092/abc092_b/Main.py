n = int(input())
d,x = map(int,input().split())
a = []

for i in range(n):
    a.append(int(input()))

for i in a:
    for j in range(1,d+1):
        if i == 1:
            x += d
            break
        elif j % i == 1:
            x += 1
print(x)