n,k = map(int,input().split())
sum_ = 0
for i in range(n):
    sum_ += int(input())
    if sum_ >= k:
        print(i + 1)
        break