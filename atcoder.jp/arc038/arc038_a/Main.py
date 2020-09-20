n = int(input())
a = [int(s) for s in input().split()]
a.sort(key=int,reverse=True)
sum_ = 0
for i in range(n):
    if i % 2 == 0:
        sum_ += a[i]
print(sum_)