s = list(input())
n = int(input())
s.sort()
dic = []
for i in range(5):
    for j in range(5):
        dic.append(s[i] + s[j])
print(dic[n - 1])