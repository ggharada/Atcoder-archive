n,m,a,b = map(int,input().split())

for i in range(m):
    tmp = int(input())
    if a >= n:
        n += b
    n -= tmp
    if n < 0:
        print(i + 1)
        break
else:
    print("complete")