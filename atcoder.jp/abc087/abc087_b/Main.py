a = int(input())
b = int(input())
c = int(input())
x = int(input())

count = 0

for i in range(a+1):
    for j in range(b+1):
        for t in range(c+1):
            if i*500 + j*100 + t*50 == x:
                count += 1
print(count)