Array1 = int(input())
Array2 = input().split()

Number = 0
times = 0

while True:
    if int(Array2[Number ]) % 2 == 0:
        Array2[Number] = int(Array2[Number]) // 2
        Number += 1
        if Number == Array1:
            Number = 0
            times += 1
    else:
        print(times)
        break