w = list(input())
output = []
for i in range(len(w)):
    if w[i] == "a" or w[i] == "i" or w[i] == "u" or w[i] == "e" or w[i] == "o":
        pass
    else:
        output.append(w[i])
print("".join(output))