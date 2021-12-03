n = int(input())
s = [int(s) for s in input().split()]

ans = 0
for i in s:
    flag = 0
    for a in range(1,1001):
        for b in range(1,1001):
            if 4 * a * b + 3 * a + 3 * b == i:
                flag = 1
    if flag is 0:
        ans += 1

print(ans)