a0 = 100
a1 = 100
a2 = 200
a3 = 0
for i in range(17):
    a3 = a0 + a1 + a2
    a0 = a1
    a1 = a2
    a2 = a3
print(a2)