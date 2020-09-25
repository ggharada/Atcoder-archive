import math

n = int(input())
x = []
y = []
for i in range(n):
    x_,y_ = map(int,input().split())
    x.append(x_)
    y.append(y_)

check = []

for i in range(n):
    for j in range(n):
        check.append(math.sqrt(pow(x[j] - x[i],2) + pow(y[j] - y[i],2)))
print(max(check))