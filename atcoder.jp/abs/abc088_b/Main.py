n = int(input())
a = [int(s) for s in input().split()]
a.sort(key=int)
alice = 0
bob = 0

for i in range(n):
    if i % 2:
        alice += a[i]
    else:
        bob += a[i]
print(abs(alice - bob))