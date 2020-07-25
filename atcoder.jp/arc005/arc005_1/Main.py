n = int(input())
check = list(input().split())
count = 0
for i in range(n):
    if check[i] == "TAKAHASHIKUN" or check[i] == "Takahashikun" or check[i] == "takahashikun" or check[i] == "TAKAHASHIKUN." or check[i] == "Takahashikun." or check[i] == "takahashikun.":
        count += 1
print(count)