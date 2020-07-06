a,b = map(int,input().split())
tmp = a * b % 2
if tmp == 0:
    print("Even")
else:
    print("Odd")