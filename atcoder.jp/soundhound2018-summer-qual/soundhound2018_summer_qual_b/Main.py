import math

s = input()
w = int(input())
for i in range(math.ceil(len(s) / w)):
    print(s[i * w],end="")
print("")