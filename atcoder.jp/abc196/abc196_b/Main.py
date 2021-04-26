x = input()
point = x.find(".")
if point != -1:
    x = x[:point]
print(x)