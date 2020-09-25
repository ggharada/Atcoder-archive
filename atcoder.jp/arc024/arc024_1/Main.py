l,r = map(int,input().split())
l_ = [int(s) for s in input().split()]
r_ = [int(s) for s in input().split()]

count = 0

for i in l_:
    for j in r_:
        if i == j:
            count += 1
            r_.remove(j)
            break
print(count)