s = list(input())
if s[0] == s[2] and s[1] == s[3]:
    print("Yes")
elif s[0] == s[1] and s[0] == s[2] and s[0] == s[3]:
    print("Yes")
else:
    print("No")