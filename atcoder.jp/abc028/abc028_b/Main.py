line = list(input())
dic = ["A","B","C","D","E","F"]
for i in range(5):
    print(str(line.count(dic[i])) + " ",end = "")
print(str(line.count(dic[5])))