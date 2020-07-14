l, h = map(int,input().split())
n = int(input())
for i in range(n):
    tmp = int(input())
    if l <= tmp <= h:
        print(0)
    elif tmp >= h:
        print(-1)
    else:
        print(l - tmp)