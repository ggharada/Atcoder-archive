n = int(input())
nuts = 0
wood = [int(s) for s in input().split()]

for i in range(n):
    if wood[i] > 10:
        nuts += wood[i] - 10
print(nuts)