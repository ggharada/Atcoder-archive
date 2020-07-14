x = int(input())
funy = 0
while x >= 500:
    x -= 500
    funy += 1000
while x >= 5:
    x -= 5
    funy += 5
print(funy)