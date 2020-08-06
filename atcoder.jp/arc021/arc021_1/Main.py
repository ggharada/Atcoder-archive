check = [list(map(int,input().split())) for _ in range(4)]
for i in range(4):
    for j in range(3):
        if check[i][j] == check[i][j + 1] or check[j][i] == check[j + 1][i]:
            print("CONTINUE")
            exit()
print("GAMEOVER")