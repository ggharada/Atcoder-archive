n = int(input())
a = []
b = []
c = []
for i in range(n):
    a_ , b_ = map(int,input().split())
    a.append(a_)
    b.append(b_)
    c.append(a_ + b_)
time = []
for i in range(n):
    for j in range(n):
        if i != j:
            time.append(max(a[i],b[j]))
if min(time) >= min(c):
    print(min(c))
else:
    print(min(time))