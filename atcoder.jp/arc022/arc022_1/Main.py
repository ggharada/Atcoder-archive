s = input()
s = s.upper()
wait = "I"
for i in range(len(s)):
    if s[i] == wait == "I":
        wait = "C"
    if s[i] == wait == "C":
        wait = "T"
    if s[i] == wait == "T":
        print("YES")
        break
else:
    print("NO")