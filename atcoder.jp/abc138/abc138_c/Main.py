n = int(input())
u = [int(s) for s in input().split()]
u.sort(reverse=True)

while len(u) != 1:
    x = u.pop()
    y = u.pop()
    u.append((x+y)/2)
print(u[0])