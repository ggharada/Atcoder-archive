s1 = input()
s2 = input()
s3 = input()
s4 = input()
ans = ["3B","HR","2B","H"]
s = list((s1,s2,s3,s4))

if 4 == len(set(ans) & set(s)):
    print("Yes")
else:
    print("No")