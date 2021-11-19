ans = ["ARC","ABC","AGC","AHC"]
for _ in range(3):
    try:
        ans.remove(input())
    except ValueError:
        pass
print("".join(ans))