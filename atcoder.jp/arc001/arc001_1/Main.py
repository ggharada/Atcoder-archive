n = int(input())
c = list(input())

ans = []
ans.append(c.count("1"))
ans.append(c.count("2"))
ans.append(c.count("3"))
ans.append(c.count("4"))
print(str(max(ans)) + " " + str(min(ans)))