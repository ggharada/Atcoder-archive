a,b = map(int,input().split())
diff = abs(b - a)
action = [0,1,2,3,2,1,2,3,3,2]
print(diff // 10 + action[diff % 10])