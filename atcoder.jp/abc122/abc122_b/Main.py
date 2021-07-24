s = input()
count = 0

for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        if all([k=='A' or k=='C' or k=='G' or k=='T' for k in s[i:j]]):
            
            count = max(count,j-i)
print(count)