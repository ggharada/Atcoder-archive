s1 = input()
s2 = input()

if s1[0] == s1[1] or s1[1] == s2[1] or s2[1] == s2[0] or s2[0] == s1[0]:
    print('Yes')
else:
    print('No')