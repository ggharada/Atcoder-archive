h,w = map(int,input().split())

array = []
minimum = 100
ans = 0

for i in range(h):
    array.append([int(s) for s in input().split()])

for i in range(h):
    if min(array[i]) < minimum:
        minimum = min(array[i])

for i in range(h):
    for j in range(w):
        ans += max(0,array[i][j]) - minimum

print(ans)