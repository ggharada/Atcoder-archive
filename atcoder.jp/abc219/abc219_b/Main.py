s1 = input()
s2 = input()
s3 = input()
t = list(input())
array = ""
for i in range(len(t)):
    if int(t[i]) == 1:
        array += s1
    elif int(t[i]) == 2:
        array += s2
    else:
        array += s3
print(array)