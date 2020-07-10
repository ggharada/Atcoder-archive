line = []
for i in range(5):
    line.append(input())
k = int(input())
if int(line[4]) - int(line[0]) <= k:
    print("Yay!")
else:
    print(":(")