n,a,x,y = map(int,input().split())
count = 0

for i in range(n):
    if a  <= i:
        count += y
    else:
        count += x
print(count)