n = int(input())
point = []

for _ in range(n):
    list_ = [int(s) for s in input().split()]
    point.append((list_[0] + list_[1] + list_[2] + list_[3]) + list_[4] * (110/900))
print(max(point))