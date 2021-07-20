n = input()
s = list(input())
locate = s.index("1")
if (locate + 1) % 2 == 0:
    print("Aoki")
else:
    print("Takahashi")