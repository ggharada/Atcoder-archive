k = int(input())
s = input()
if len(s) <= k:
    print(s)
else:
    print(str(s[0:k]) + "...")