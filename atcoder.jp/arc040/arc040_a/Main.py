R = 0
B = 0
for i in range(int(input())):
    tmp = input()
    for i in range(len(tmp)):
        if tmp[i] == "R":
            R += 1
        elif tmp[i] == "B":
            B += 1
if R == B:
    print("DRAW")
elif R > B:
    print("TAKAHASHI")
else:
    print("AOKI")