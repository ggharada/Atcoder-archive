n = int(input())
name = []
height = []
for i in range(n):
    n,h = map(str,input().split())
    name.append(n)
    height.append(int(h))
m = max(height)
i = height.index(m)
height[i] = 0
m = max(height)
i = height.index(m)
print(name[i])