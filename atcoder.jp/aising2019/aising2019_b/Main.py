n = int(input())
a,b = map(int,input().split())
p = [int(s) for s in input().split()]

q1 = 0
q2 = 0
q3 = 0

for i in range(n):
    if p[i] <= a:
        q1 += 1
    if a < p[i] <= b:
        q2 += 1
    if b < p[i]:
        q3 += 1
print(min(q1,q2,q3))