n,q = map(int,input().split())
line = [0] * 110
tmp = []
for _ in range(q):
    tmp = list(map(int,input().split()))
    for i in range(tmp[1] - tmp[0] + 1):
        line[tmp[0] + i] = tmp[2]
for j in range(n):
    print(line[j + 1])