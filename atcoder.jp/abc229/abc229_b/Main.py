a,b = map(str, input().split())
a = list(a)[::-1]
b = list(b)[::-1]

for i in range(min(len(a),len(b))):
    if int(a[i]) + int(b[i]) >= 10:
        print("Hard")
        exit()
print("Easy")