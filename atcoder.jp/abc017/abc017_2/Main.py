x = input()
x = x.replace("ch","")
x = x.replace("o","")
x = x.replace("k","")
x = x.replace("u","")

print("YES") if len(x) == 0 else print("NO")