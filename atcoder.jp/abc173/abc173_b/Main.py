n = int(input())
ac = 0
wa = 0
tle = 0
re = 0
for i in range(n):
    tmp = input()
    if tmp == "AC":
        ac += 1
    elif tmp == "WA":
        wa += 1
    elif tmp == "TLE":
        tle += 1
    else:
        re += 1
print("AC x " + str(ac))
print("WA x " + str(wa))
print("TLE x " + str(tle))
print("RE x " + str(re))