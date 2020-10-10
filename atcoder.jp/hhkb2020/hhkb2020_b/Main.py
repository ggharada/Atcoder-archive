h,w = map(int,input().split())
s = []
for i in range(h):
    s.append(input())
count = 0
for i in range(h):
    for j in range(w):
        if j < w-1:
            if s[i][j] == "." and s[i][j+1] == ".":
                count += 1
        if i < h-1:
            if s[i][j] == "." and s[i+1][j] == ".":
                count += 1
print(count)