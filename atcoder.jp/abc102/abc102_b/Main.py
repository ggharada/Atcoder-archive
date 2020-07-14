n = int(input())
a = list(input().split())
a.sort(key=int)
print(int(a[-1]) - int(a[0]))