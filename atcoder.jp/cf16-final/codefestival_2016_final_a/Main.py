h,w = map(int,input().split())
for i in range(h):
    tmp = list(input().split())
    for j in range(w):
        if tmp[j] == "snuke":
            num2alpha = lambda c: chr(c+64)
            print(num2alpha(j + 1) + str(i + 1))
